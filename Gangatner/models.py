from django.db import models
from Grancum.models import Գրանցում
# Create your models here.
class Գանգաթներ(models.Model):
    gg = models.ForeignKey(Գրանցում, on_delete = models.CASCADE)
    տարի = models.IntegerField(null=True, blank=True)
    ամիս = models.IntegerField(null=True, blank=True)
    օր = models.IntegerField(null=True, blank=True)
    գանգաթներ = models.CharField(max_length=3000,null=True, blank=True, verbose_name='Գանգաթներ')