from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import Info, Kpp
from .serializers import KppSerializerr, InfoSerializer, CommentsSerzr, InfoParserSerializer
from django.db.models import Max, F, Count, Prefetch
from django.db.models.functions import Length
from django.db import connection
from datetime import datetime
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from config.settings import COMMENTS_FETCH_COUNT
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'front/index.html')


class KppInfo(APIView):

    @method_decorator(cache_page(30))  # 60 сек кэш
    def get(self, request):
        kpps = Kpp.objects.prefetch_related('info').select_related('name')
        ksr = KppSerializerr(kpps, many=True)
        data = ksr.data
        # print(data)
        # return Response(data)
        return JsonResponse(data, safe=False)

    def post(self, request):
        context = {
            'is_admin': request.user.is_superuser,
            'is_parser': False,
        }
        serializer = InfoSerializer(data=request.data, context=context)
        if serializer.is_valid():
            # print(serializer.validated_data)
            # serializer.save(data=request.data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Telega(APIView):

    def post(self, request):
        serializer = InfoParserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Comments(APIView):

    @method_decorator(cache_page(30))  # 60 сек кэш
    def get(self, request):
        after_date = request.query_params.get('after_date')
        if not after_date:
            qs = Info.objects.annotate(comment_len=Length('comment')).filter(
                approved=True,
                comment_len__gt=0,
                comment_approved=True,
            ).order_by('-added')[:COMMENTS_FETCH_COUNT]
        else:
            date = datetime.fromisoformat(after_date.replace("Z", "+00:00"))
            qs = Info.objects.annotate(comment_len=Length('comment')).filter(
                approved=True,
                comment_len__gt=0,
                added__gt=date,
                comment_approved=True,
            ).order_by('-added')[:COMMENTS_FETCH_COUNT]

        srzr = CommentsSerzr(qs, many=True)
        return Response(srzr.data)
