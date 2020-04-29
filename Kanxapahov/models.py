from django.db import models
from Grancum.models import Գրանցում
# Create your models here.
class Կանխապահով(models.Model):
    այդի = models.ForeignKey(Գրանցում, on_delete = models.CASCADE)
    aԱմիս = models.IntegerField()
    tՏարի = models.IntegerField()
    oօր = models.IntegerField()
    Պատվաստանյութ = models.CharField(max_length=10000)
    Դոզա = models.CharField(max_length=10000)
    Ազդեցություն = models.CharField(max_length=10000)

