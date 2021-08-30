# Generated by Django 3.2.4 on 2021-06-05 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Kpp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_ldnr', models.BooleanField(default=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kpp', to='kppshka.name')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cars_num', models.PositiveIntegerField(default=0)),
                ('car_type', models.PositiveIntegerField(default=0)),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('comment', models.CharField(blank=True, max_length=256, null=True)),
                ('approved', models.BooleanField(default=False)),
                ('kpp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='info', to='kppshka.kpp')),
            ],
        ),
    ]
