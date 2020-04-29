from django.db import models
from Grancum.models import Գրանցում
# Create your models here.
class Առողջական(models.Model):
    tt = models.ForeignKey(Գրանցում, on_delete=models.CASCADE)
    տարրիիի = models.IntegerField()
    ամիիսսս = models.IntegerField()
    օօրրր = models.IntegerField()
    Ախտորոշու = models.CharField(max_length=10000)
    ԱԱռողջական = models.CharField(max_length=10000)
    Հաշվառվել = models.CharField(max_length=10000)
    Ֆիզպատ = models.CharField(max_length=10000)