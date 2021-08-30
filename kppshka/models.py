from django.db import models


class Name(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Kpp(models.Model):
    name = models.ForeignKey(Name, related_name='kpp', on_delete=models.CASCADE)
    from_ldnr = models.BooleanField(default=True)  # Направление в РФ

    def __str__(self):
        return self.name.name + (' в РФ' if self.from_ldnr else ' из РФ')


class Info(models.Model):
    kpp = models.ForeignKey(Kpp, related_name='info', on_delete=models.CASCADE, verbose_name='КПП')
    cars_num = models.PositiveIntegerField(default=0, verbose_name='Машин')
    car_type = models.PositiveIntegerField(default=0, verbose_name='Тип')
    added = models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')
    comment = models.CharField(max_length=256, null=True, blank=True, verbose_name='Коммент')
    approved = models.BooleanField(default=False, verbose_name='Одобрено')
    comment_approved = models.BooleanField(default=True, verbose_name='Камент одобрен')
