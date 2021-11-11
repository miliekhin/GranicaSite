# Generated by Django 3.2.4 on 2021-06-05 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kppshka', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info',
            name='added',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Добавлено'),
        ),
        migrations.AlterField(
            model_name='info',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Одобрено'),
        ),
        migrations.AlterField(
            model_name='info',
            name='car_type',
            field=models.PositiveIntegerField(default=0, verbose_name='Тип'),
        ),
        migrations.AlterField(
            model_name='info',
            name='cars_num',
            field=models.PositiveIntegerField(default=0, verbose_name='Машин'),
        ),
        migrations.AlterField(
            model_name='info',
            name='comment',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Коммент'),
        ),
        migrations.AlterField(
            model_name='info',
            name='kpp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='kppshka.kpp', verbose_name='КПП'),
        ),
    ]