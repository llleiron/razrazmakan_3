from django.db import models
from Grancum.models import Գրանցում
# Create your models here.

class Վիճակ(models.Model):
    idi = models.ForeignKey(Գրանցում, on_delete=models.CASCADE)
    tttaaarrriii = models.IntegerField()
    ooorrr = models.IntegerField()
    aaammmiiisss = models.IntegerField()
    information = models.CharField(max_length=100000)
    