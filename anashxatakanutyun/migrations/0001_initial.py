# Generated by Django 2.0.12 on 2020-04-14 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Grancum', '0008_auto_20200409_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anashxatakanutyun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yyeeaarr', models.IntegerField()),
                ('mmoonntthh', models.IntegerField()),
                ('ddaayy', models.IntegerField()),
                ('yearend', models.IntegerField()),
                ('monthend', models.IntegerField()),
                ('dayend', models.IntegerField()),
                ('himnakan', models.CharField(max_length=10000)),
                ('ambulator', models.IntegerField()),
                ('stacionar', models.IntegerField()),
                ('hivanducyan', models.IntegerField()),
                ('full', models.IntegerField()),
                ('ididid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grancum.Գրանցում')),
            ],
        ),
    ]
