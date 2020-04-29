from django.db import models
from Grancum.models import Գրանցում
# Create your models here.

class Anashxatakanutyun(models.Model):
    ididid = models.ForeignKey(Գրանցում, on_delete=models.CASCADE)
    yyeeaarr = models.IntegerField()
    mmoonntthh = models.IntegerField()
    ddaayy = models.IntegerField()
    yearend = models.IntegerField()
    monthend = models.IntegerField()
    dayend = models.IntegerField()
    himnakan = models.CharField(max_length=10000)
    ambulator = models.IntegerField()
    stacionar = models.IntegerField()
    hivanducyan = models.IntegerField()
    full = models.IntegerField()
