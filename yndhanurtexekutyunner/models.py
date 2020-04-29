from django.db import models
from Grancum.models import Գրանցում

# Create your models here.
class ԸնդհանուրՏեղեկություններ(models.Model):
    հհ = models.ForeignKey(Գրանցում, on_delete = models.CASCADE, null=True, blank=True, unique=True)
    Զինկոչումը = models.CharField(max_length=32,verbose_name='Զինկոչումը',null=True, blank=True)
    ԱրյանԽումբը = models.CharField(max_length=32,verbose_name='Արյան խումբը',null=True, blank=True)
    ԾննդյանՏարեթիվը = models.DateField(verbose_name='Ծննդյան տարեթիվը',null=True, blank=True)
    Ազգությունը = models.CharField(max_length=32,verbose_name='Ազգությունը',null=True, blank=True)
    Կրթությունը = models.CharField(max_length=1000,verbose_name='Կրթությունը', help_text='ընդհանուր, զինվորական, հատուկ մասնագիտական',null=True, blank=True)
    ԾառայությանԱնցնելուԱմսաթիվը = models.DateField(verbose_name='Ծառայության անցնելու ամսաթիվը',null=True, blank=True)
    ԸնտանեկանԴրությունը =  models.TextField(verbose_name='Ընտանեկան դրություն', max_length=1000, help_text='ամուրի, ամուսնացած, երեխաների և խնամակյալների թիվը',null=True, blank=True)
    ՏանՀասցեն = models.CharField(verbose_name='Տան հասցեն', max_length=300,null=True, blank=True)
    ՏանՀեռախոսահամարը = models.IntegerField(verbose_name='Տան հեռախոսահամարը',null=True, blank=True, help_text='+***********')
    ԾառայավայրիՀասցեն = models.TextField(verbose_name='Ծառայավայրի հասցեն', max_length=300,null=True, blank=True)
    ԾառայավայրիՀեռախոսահամարը = models.IntegerField(verbose_name='Ծառայավայրի հեռախոսահամարը', null=True, blank=True, help_text='+***********')
    def __str__(self):
        return str(self.հհ)