from django.db import models
from Grancum.models import Գրանցում

class Ֆիզիկական(models.Model):
    oo = models.ForeignKey(Գրանցում, on_delete = models.CASCADE)
    Տարիի = models.IntegerField()
    Ամիսս = models.IntegerField()
    Օրր = models.IntegerField()
    Քաշը = models.IntegerField()
    Հասակը = models.IntegerField()
    ԿրծքավանդակՀանգիստ = models.CharField(max_length=100)
    ԿրծքավանդակՇնչելիս = models.CharField(max_length=100)
    ԿրծքավանդակԱրտաշնչելիս = models.CharField(max_length=100)
    ՓորիՇրջագիծը = models.IntegerField()
    Շնչաչափը = models.IntegerField()
    Աջ = models.IntegerField()
    Ձախ = models.IntegerField()