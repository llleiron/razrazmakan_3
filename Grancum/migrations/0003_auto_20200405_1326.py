# Generated by Django 2.0.12 on 2020-04-05 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Grancum', '0002_auto_20200403_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='գրանցում',
            name='Ազգանուն',
            field=models.CharField(default=1, max_length=32, verbose_name='Ազգանուն'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='գրանցում',
            name='Անուն',
            field=models.CharField(default=1, max_length=32, verbose_name='Անուն'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='գրանցում',
            name='ԳրանցմանԱմսաթիվ',
            field=models.DateField(auto_now=True, default = '2019-10-10'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='գրանցում',
            name='Հայրանուն',
            field=models.CharField(default=1, max_length=32, verbose_name='Հայրանուն'),
            preserve_default=False,
        ),
    ]
