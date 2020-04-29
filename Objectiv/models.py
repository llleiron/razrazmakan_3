from django.db import models
from Grancum.models import Գրանցում
# Create your models here.
class Օբյեկտիվ(models.Model):
    bb = models.ForeignKey(Գրանցում, on_delete=models.CASCADE)
    Տարիիի = models.IntegerField()
    Ամիսսս = models.IntegerField()
    Օրրր = models.IntegerField()
    Մարմնակազմությունը = models.CharField(max_length=5000)
    ԻնչպեսԷՍնվում = models.CharField(max_length=5000)
    ՖիզիկականԱրատներ = models.CharField(max_length=5000)
    ՄարմնիԾածկույթը = models.CharField(max_length=5000)
    Լիմֆատիկ = models.CharField(max_length=5000)
    Ոսկրամկանային = models.CharField(max_length=5000)
    էնդոկրին = models.CharField(max_length=5000)
    Շնչառական = models.CharField(max_length=5000)
    Արյուն = models.CharField(max_length=5000)
    հանգզարկ = models.CharField(max_length=5000)
    հանգզարկառ = models.CharField(max_length=5000)
    հանգզարկնվազ = models.CharField(max_length=5000)
    կքնզարկ = models.CharField(max_length=5000)
    կքնզարկառ = models.CharField(max_length=5000)
    կքնզարկնվազ = models.CharField(max_length=5000)
    րոպեզարկ = models.CharField(max_length=5000)
    րոպեզարկառ = models.CharField(max_length=5000)
    րոպեզարկնվազ = models.CharField(max_length=5000)
    մարս = models.CharField(max_length=5000)
    լյարդ = models.CharField(max_length=5000)
    փայծ = models.CharField(max_length=5000)
    միզասեռ = models.CharField(max_length=5000)
    Նյարդ = models.CharField(max_length=5000)
    տեսողություն = models.CharField(max_length=5000)
    լսողություն = models.CharField(max_length=5000)
    Բժիշկ = models.CharField(max_length=5000)
    Վիրաբուժ = models.CharField(max_length=5000)
    եզր = models.CharField(max_length=5000)