# Generated by Django 2.0.12 on 2020-04-04 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yndhanurtexekutyunner', '0003_ընդհանուրտեղեկություններ_հհ'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ընդհանուրտեղեկություններ',
            name='հհ',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Grancum.Գրանցում', unique=True),
        ),
    ]