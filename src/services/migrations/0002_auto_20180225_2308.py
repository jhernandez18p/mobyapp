# Generated by Django 2.0 on 2018-02-26 04:08

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='background',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='service/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='service/'),
        ),
        migrations.AlterField(
            model_name='serviceimage',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, upload_to='service/'),
        ),
    ]
