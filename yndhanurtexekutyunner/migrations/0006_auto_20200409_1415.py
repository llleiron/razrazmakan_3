# Generated by Django 2.0.12 on 2020-04-09 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yndhanurtexekutyunner', '0005_auto_20200409_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ընդհանուրտեղեկություններ',
            name='ԾառայությանԱնցնելուԱմսաթիվը',
            field=models.DateField(blank=True, null=True, verbose_name='Ծառայության անցնելու ամսաթիվը'),
        ),
        migrations.AlterField(
            model_name='ընդհանուրտեղեկություններ',
            name='ԾննդյանՏարեթիվը',
            field=models.DateField(blank=True, null=True, verbose_name='Ծննդյան տարեթիվը'),
        ),
    ]
