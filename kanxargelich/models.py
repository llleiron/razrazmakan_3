from django.db import models
from Grancum.models import Գրանցում
# Create your models here.
class Բուժկանխարգելիչ(models.Model):
    jo = models.ForeignKey(Գրանցում, on_delete=models.CASCADE)
    ՕՕՕրրր = models.IntegerField()
    ԱԱԱմիսսս = models.IntegerField()
    ՏՏՏարիիի = models.IntegerField()
    Նշանակված = models.CharField(max_length=10000)
    Բուժկանխարգելիչմ = models.CharField(max_length=10000)
    Զորամաս = models.CharField(max_length=10000)