from django.db import models
from Grancum.models import Գրանցում


class Ծառայություն(models.Model):
    ll = models.ForeignKey(Գրանցում, on_delete = models.CASCADE)
    ԾառայութայնԵվԿենցաղայինՊայմանները = models.TextField(max_length=1000, verbose_name='Ծառայության և կենցաղային պայմանները',null=True, blank=True)
    ԱշխատանքիԲնույթը = models.TextField(max_length=1000, verbose_name='Աշխատանքի բնույթը',null=True, blank=True, help_text='շարային, շտաբային, մանկավարժական և այլն')
    ԲնակկենցաղայինՊայմանները = models.TextField(max_length=1000, verbose_name='Բնակենցաղային պայմանների բնութագիրը',null=True, blank=True)
    Սնունդը = models.TextField(max_length=1000, verbose_name='Սնունդը',null=True, blank=True, help_text='կանոնավոր, անկանոն, օրը քանի անգամ, դիետիկ')
    Քունը = models.TextField(max_length=1000, verbose_name='Քնի տևողությունը և բնույթը',null=True, blank=True)
    ՖիզիկականՊատրաստությունը = models.TextField(max_length=1000, verbose_name='Ֆիզիկական պատրաստությունը։ Ինքնուրույն մարզումները',null=True, blank=True, help_text='պարբերաբար, անկանոն')
    Արձակուրդը = models.TextField(max_length=1000, verbose_name='Արձակուրդը',null=True, blank=True, help_text='որտեղ, երբ է անցկացրել, որ հանգստյան տանը, առողջարանում, տուրիստական արշավում և այլն')
    year = models.IntegerField(null=True, blank=True)
    month = models.IntegerField(null=True, blank=True)
    day = models.IntegerField(null=True, blank=True)