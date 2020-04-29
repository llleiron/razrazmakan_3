# Generated by Django 2.0.12 on 2020-04-14 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Grancum', '0008_auto_20200409_1514'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ատամնաբուժական',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tari', models.IntegerField()),
                ('Amis', models.IntegerField()),
                ('Or', models.IntegerField()),
                ('info', models.CharField(max_length=10000)),
                ('ok', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Grancum.Գրանցում')),
            ],
        ),
    ]