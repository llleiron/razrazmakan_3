from django.db import models
from Grancum.models import Գրանցում
class ՄյուսՄասնագետներ(models.Model):
    pa = models.ForeignKey(Գրանցում, on_delete=models.CASCADE)
    Տարրի = models.IntegerField()
    Ամիիս = models.IntegerField()
    Օօր = models.IntegerField()
    Մյուս = models.TextField(max_length=10000)