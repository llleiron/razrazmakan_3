from django.db import models
from Grancum.models import Գրանցում
# Create your models here.

class Ատամնաբուժական(models.Model):
    ok = models.ForeignKey(Գրանցում, on_delete=models.CASCADE)
    Tari = models.IntegerField()
    Amis = models.IntegerField()
    Or = models.IntegerField()
    info = models.CharField(max_length=10000)