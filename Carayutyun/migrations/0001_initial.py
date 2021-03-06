# Generated by Django 2.0.12 on 2020-04-10 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Grancum', '0008_auto_20200409_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ծառայություն',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ԾառայութայնԵվԿենցաղայինՊայմանները', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Ծառայության և կենցաղային պայմանները')),
                ('ԱշխատանքիԲնույթը', models.TextField(blank=True, help_text='շարային, շտաբային, մանկավարժական և այլն', max_length=1000, null=True, verbose_name='Աշխատանքի բնույթը')),
                ('ԲնակկենցաղայինՊայմանները', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Բնակենցաղային պայմանների բնութագիրը')),
                ('Սնունդը', models.TextField(blank=True, help_text='կանոնավոր, անկանոն, օրը քանի անգամ, դիետիկ', max_length=1000, null=True, verbose_name='Սնունդը')),
                ('Քունը', models.TextField(blank=True, max_length=1000, null=True, verbose_name='Քնի տևողությունը և բնույթը')),
                ('ՖիզիկականՊատրաստությունը', models.TextField(blank=True, help_text='պարբերաբար, անկանոն', max_length=1000, null=True, verbose_name='Ֆիզիկական պատրաստությունը։ Ինքնուրույն մարզումները')),
                ('Արձակուրդը', models.TextField(blank=True, help_text='որտեղ, երբ է անցկացրել, որ հանգստյան տանը, առողջարանում, տուրիստական արշավում և այլն', max_length=1000, null=True, verbose_name='Արձակուրդը')),
                ('year', models.IntegerField(blank=True, null=True)),
                ('month', models.IntegerField(blank=True, null=True)),
                ('day', models.IntegerField(blank=True, null=True)),
                ('հհ', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grancum.Գրանցում')),
            ],
        ),
    ]
