from django.contrib import admin
from .models import Info, Kpp, Name
import pytz


@admin.register(Info)
class KppshkaAdmin(admin.ModelAdmin):
    list_display = ('kpp', 'cars_num', 'car_type', 'comment', 'approved', 'comment_approved', 'added_time',)
    # list_editable = ('cars_num', 'approved', 'comment_approved',)

    def added_time(self, info):
        tz = pytz.timezone("Europe/Moscow")
        dt = info.added.astimezone(tz)
        fmt = '%d.%m.%Y_%H:%M'
        return dt.strftime(fmt)

    added_time.short_description = 'Добавлен'


@admin.register(Kpp)
class KppshkaAdmin(admin.ModelAdmin):
    list_display = ('name', 'from_ldnr', )


@admin.register(Name)
class KppshkaAdmin(admin.ModelAdmin):
    list_display = ('name', )
