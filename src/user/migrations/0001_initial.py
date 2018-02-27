# Generated by Django 2.0 on 2018-02-16 10:16

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Frecuency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('average', models.CharField(blank=True, max_length=144)),
                ('monday', models.CharField(blank=True, max_length=144)),
                ('tuesday', models.CharField(blank=True, max_length=144)),
                ('wednesday', models.CharField(blank=True, max_length=144)),
                ('thursday', models.CharField(blank=True, max_length=144)),
                ('friday', models.CharField(blank=True, max_length=144)),
                ('saturday', models.CharField(blank=True, max_length=144)),
                ('sunday', models.CharField(blank=True, max_length=144)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Frecuencia de visita',
                'verbose_name_plural': 'Frecuencia de visitas',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=144)),
                ('bio', ckeditor.fields.RichTextField(blank=True)),
                ('description', ckeditor.fields.RichTextField(blank=True)),
                ('member_since', models.CharField(blank=True, max_length=144)),
                ('direction1', ckeditor.fields.RichTextField(blank=True)),
                ('direction2', ckeditor.fields.RichTextField(blank=True)),
                ('phone', models.CharField(blank=True, max_length=144)),
                ('is_active', models.CharField(blank=True, max_length=144)),
                ('respons', models.CharField(blank=True, max_length=144)),
                ('country', models.CharField(blank=True, max_length=144)),
                ('city', models.CharField(blank=True, max_length=144)),
                ('zip_code', ckeditor.fields.RichTextField(blank=True)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_buyer', models.BooleanField(default=True)),
                ('is_provider', models.BooleanField(default=False)),
                ('seller_description', ckeditor.fields.RichTextField(blank=True)),
                ('score', models.CharField(blank=True, max_length=144)),
                ('saldo', models.CharField(blank=True, max_length=144)),
                ('max_credit', models.CharField(blank=True, max_length=144)),
                ('payment_lapse', models.CharField(blank=True, max_length=144)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.Profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil de usuario',
                'verbose_name_plural': 'Perfiles de usuarios',
            },
        ),
    ]