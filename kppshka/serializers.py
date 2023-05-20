from rest_framework import serializers
from .models import Info, Kpp, Name
from django.core.exceptions import ObjectDoesNotExist
from config.settings import CARS_MAX_COUNT, MAX_COMMENT_LENGTH, CARS_MAX_WARNING, TELEGRAM_BOT_TOKEN, CHAT_ID
import httpx
import re


def send_telegram_message(msg):
    try:
        url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}'
        httpx.get(url)
    except httpx.RequestError:
        print('An error occurred while requesting Telegram')


def is_incoming_data_correct(validated_data):
    cars = validated_data['cars_num']
    if int(cars) >= CARS_MAX_COUNT:
        return False

    if int(cars) >= CARS_MAX_WARNING:
        car_type = 'Легковые'
        if int(validated_data['car_type']) == 1:
            car_type = 'Грузовые'
        msg = f'КППШка: количество машин в запросе из формы {cars} превышает {CARS_MAX_WARNING}. Тип: {car_type}'
        send_telegram_message(msg)

    comment = validated_data['comment']
    warn_obj = re.search(r'ху[еёй]|п[ие]зд|[ёеб]а|пид[ао]р', comment)
    if warn_obj:
        print('Obscene language detected')
        send_telegram_message(f'КППШка: комент отклонен: {comment}')
        return False
    return True


def received_data_validator(data):
    # Здесь проводится валидация и эти данные попадают в create
    if int(data['car_type']) > 1:
        raise serializers.ValidationError({'Неверный тип транспорта:': data['car_type']})
    if int(data['cars_num']) > CARS_MAX_COUNT:
        raise serializers.ValidationError({f'Количество машин {data["cars_num"]} больше допустимого': CARS_MAX_COUNT})
    if len(data['comment']) > MAX_COMMENT_LENGTH:
        raise serializers.ValidationError({'Комментарий слишком длинный': len(data['comment'])})


class InfoParserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        fields = '__all__'

    def create(self, validated_data):
        try:
            from_ldnr = (validated_data.get('way') == 'to_rf')
            nm = validated_data.get('kpp_name')
            nm = Name.objects.get(name=nm)
            kpp = Kpp.objects.get(name=nm, from_ldnr=from_ldnr)
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'КПП не найден': validated_data["kpp_name"]})

        cars = int(validated_data.get('cars_num'))
        if cars < 0:
            cars = 0
        comment = validated_data.get('comment')
        if int(cars) >= CARS_MAX_WARNING:
            send_telegram_message(f'КППШка: количество машин в запросе '
                                  f'телеграм-парсера {cars} превышает {CARS_MAX_WARNING} '
                                  f'Комент: {comment}'
                                  )
        recognition_result = validated_data.get('recognition_result')
        if recognition_result != 'accept':
            send_telegram_message(f'КППШка: Комент не распознан: {comment}')
        inf = Info.objects.create(
            kpp=kpp,
            cars_num=cars,
            car_type=validated_data.get('car_type'),
            comment=comment,
            approved=recognition_result == 'accept',
            comment_approved=False,
        )
        return inf

    def to_internal_value(self, data):
        received_data_validator(data)

        ret = {
            'car_type': data['car_type'],
            'comment': data['comment'],
            'cars_num': data['cars_num'],
            'kpp_name': data['kpp_name'],
            'way': data['way'],
            'recognition_result': data['recognition_result'],
        }

        return ret


class InfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Info
        exclude = ['id', 'approved', 'comment_approved', 'comment', 'kpp']

    # def validate_car_type(self, value):
    #     if value > 1:
    #         raise serializers.ValidationError('Неверный тип транспорта')
    #     return value

    def create(self, validated_data):
        try:
            kpp = Kpp.objects.get(id=validated_data['kpp'])
        except ObjectDoesNotExist:
            raise serializers.ValidationError({'КПП не найден': validated_data["kpp_name"]})

        if self.context['is_admin']:
            print('Admin added new info')
            approved = True
        else:
            print('Anonymous user added new info')
            approved = is_incoming_data_correct(validated_data)

        comment = validated_data['comment']
        if comment and len(comment) <= 4:
            comment = ''

        car_type = validated_data['car_type']
        cars = validated_data['cars_num']
        if len(comment):
            send_telegram_message(f'КППШка: добавлен комент: {comment}; КПП: {kpp}; ТИП: {car_type}; МАШИН: {cars}')

        inf = Info.objects.create(
            kpp=kpp,
            cars_num=cars,
            car_type=car_type,
            comment=comment,
            approved=approved,
            comment_approved=not self.context['is_parser'],
        )
        # print('context', self.context['is_admin'])
        return inf

    def to_internal_value(self, data):
        received_data_validator(data)
        # print(data)
        return data

    # def to_representation(self, info):
    #     return {
    #         'id': info.id,
    #         'name': info.name,
    #     }


def get_info_data(infos_qs):
    count = infos_qs.count()
    # trend_up = False

    if count:
        # if count > 1:
        #     if infos_qs[0].cars_num - infos_qs[1].cars_num > 0:
        #         trend_up = True
        # info = InfoSerializer(infos_qs[0]).data
        info = InfoSerializer(infos_qs, many=True).data
        # print('INFO:', info)
        # info['trend_up'] = trend_up
        return info
    return None


class KppSerializerr(serializers.ModelSerializer):
    # name = serializers.StringRelatedField(read_only=True)
    # queryset = Info.objects.filter(car_type=0).order_by('-added')[:2]
    # info = InfoSerializer(many=True)

    class Meta:
        model = Kpp
        fields = ['info', 'name', 'id', 'from_ldnr']

    def to_representation(self, kpp):
        kpp_obj = {
            'id': kpp.id,
            'name': kpp.name.name,
            'from_ldnr': kpp.from_ldnr,
        }
        cars = kpp.info.filter(car_type=0, approved=True).order_by('-added')[:8]
        trucks = kpp.info.filter(car_type=1, approved=True).order_by('-added')[:8]
        kpp_obj['data_cars'] = get_info_data(cars)
        kpp_obj['data_trucks'] = get_info_data(trucks)
        return kpp_obj


class CommentsSerzr(serializers.ModelSerializer):
    header = serializers.SerializerMethodField()

    class Meta:
        model = Info
        fields = ['comment', 'added', 'header']

    def get_header(self, info_obj):
        car_type = 'Легковые'
        if info_obj.car_type == 1:
            car_type = 'Грузовые'
        way = f'в сторону {("РФ" if info_obj.kpp.from_ldnr else "ДНР")}'
        h = f'{info_obj.kpp.name.name}, {way}. {car_type}: {info_obj.cars_num}'
        return h
