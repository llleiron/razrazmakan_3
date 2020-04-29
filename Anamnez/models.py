from django.db import models
from Grancum.models import Գրանցում
# Create your models here.
class Անամնեզ(models.Model):
    ՀՀ = models.ForeignKey(Գրանցում, on_delete = models.CASCADE, null=True, blank=True, unique=True)
    ՀիվանդացելԷ = models.TextField(max_length=1000, verbose_name='1․ Հիվանդացել է', null=True, blank=True, help_text='հիվանդությունը, որ տարիքում')
    վիրավորումները = models.TextField(max_length=1000, verbose_name='2․ա) վիրավորումները', null=True, blank=True)
    Կոնտուզիաները = models.TextField(max_length=1000, verbose_name='2․բ) կոնտուզիաները', null=True, blank=True)
    Վիրահատությունները = models.TextField(max_length=1000, verbose_name='3․ Վիրահատությունները', null=True, blank=True)
    ԱրձակուրդներըՀիվանդությանՊատճառով = models.TextField(max_length=1000, verbose_name='4. Արձակուրդները հիվանդությունների պատճառով',null=True, blank=True)
    ԲուժումնԱռողջարաններում = models.TextField(max_length=1000, verbose_name='5. Բուժումն առողջարաններում',null=True, blank=True)
    Ժառանգականությունը = models.TextField(max_length=1000, verbose_name='6. Ժառանգականությունը',null=True, blank=True, help_text='ընտանեկան անամնեզ')
    ԻնչԴեղերՉիԿարողանումԸնդունել = models.TextField(max_length=1000, verbose_name='7. Ինչ դեղեր չի կարողանում ընդունել',null=True, blank=True)
    ՆերարկումներիԱզդեցությունը = models.TextField(max_length=1000, verbose_name='8. Ներարկումների ազդեցությունը',null=True, blank=True, help_text='օրգանիզմի արձագանքը')
    ՎնասակարՍովորությունները = models.TextField(max_length=1000, verbose_name='9. Վնասակար սովորությունները',null=True, blank=True, help_text='խմել, ծխել և այլն')
    ՀատուկՆշումներ = models.TextField(max_length=1000, verbose_name='10. Հատուկ նշումներ',null=True, blank=True)
    def __str__(self):
        return str(self.ՀՀ)