# Generated by Django 2.0.12 on 2020-04-10 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Գանգաթներ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('տարի', models.IntegerField(blank=True, null=True)),
                ('ամիս', models.IntegerField(blank=True, null=True)),
                ('օր', models.IntegerField(blank=True, null=True)),
                ('գանգաթներ', models.CharField(blank=True, max_length=3000, null=True, verbose_name='Գանգաթներ')),
            ],
        ),
    ]