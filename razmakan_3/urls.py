from django.contrib import admin
from django.urls import path, re_path
from Grancum.views import list_grancumner, grancum_details, client, cllient, clllient
from homepage.views import homepage
from yndhanurtexekutyunner.views import clllllient, cllllient, list_yndhanurner, yndhanur_details
from Anamnez.views import cllllllient, list_anamnez, anamnez_details
from Carayutyun.views import index, carayutyun_details, list_carayutyunner, CarayutyunCreateAPIView
from Gangatner.views import gangat, list_gangatner, gangatner_details, GangatnerCreateAPIView
from Fizikakan.views import FizikakanCreateAPIView, indexx, list_fizikakanner, fizikakan_details
from Objectiv.views import ObjectivCreateAPIView, indexxx, list_objectivner, objectiv_details
from Myus.views import MyusCreateAPIView, myus, list_myusner, myus_details
from aroxjakan.views import AroxjakanCreateAPIView, aroxjakan, aroxjakan_details, list_aroxjakanner
from kanxargelich.views import KanxargelichCreateAPIView, kanxargelich, list_kanxargelichner, kanxargelich_details
from atam.views import AtamnabujakanCreateAPIView, atam, list_atamnabujakanner, atamnabujakan_details
from Kanxapahov.views import KanxapahovCreateAPIView, kanxapahov, list_kanxapahovner, kanxapahov_details
from vichak.views import VichakCreateAPIView, vichak_details, list_vichakner, Vichak
from anashxatakanutyun.views import AnashxatakanutyunCreateAPIView, anashxatakanutyun_details, list_anashxatakanutyunner, Anashxatakanutyunnk
urlpatterns = [
        path('admin/', admin.site.urls),
    path('backend/Grancum',  list_grancumner),
    path('Grancum/list', cllient),
    re_path('backend/Grancum/(?P<id>\w+)/$', grancum_details),
    path('Grancum/', client),
    re_path('Grancum/update', clllient),
        path('backend/yndhanur', list_yndhanurner),
    re_path('backend/yndhanur/(?P<հհ>\w+)/$', yndhanur_details),
    re_path('Yndhanur', cllllient),
    re_path('update/yndhanur', clllllient),
        path('backend/anamnez', list_anamnez),
    re_path('backend/anamnez/(?P<ՀՀ>\w+)/$', anamnez_details),
    re_path('Anamnez', cllllllient),
        path('carayutyun/list', list_carayutyunner),
    path('carayutyun/detail/<int:ll>/<int:year>', carayutyun_details),
    path('carayutyun/create', CarayutyunCreateAPIView.as_view()),
    path('carayutyun/', index),
        path('gangatner/list', list_gangatner),
    path('gangatner/detail/<int:gg>/<int:տարի>', gangatner_details),
    path('gangatner/create', GangatnerCreateAPIView.as_view()),
    path('gangatner/', gangat),
        path('fizikakan/list', list_fizikakanner),
    path('fizikakan/detail/<int:oo>/<int:Տարիի>', fizikakan_details),
    path('fizikakan/create',FizikakanCreateAPIView.as_view()),
    path('fizikakan/', indexx),
        path('objectiv/list', list_objectivner),
    path('objectiv/detail/<int:bb>/<int:Տարիիի>', objectiv_details),
    path('objectiv/create', ObjectivCreateAPIView.as_view()),
    path('objectiv/', indexxx),
        path('myus/list', list_myusner),
    path('myus/detail/<int:pa>/<int:Տարրի>', myus_details),
    path('myus/create', MyusCreateAPIView.as_view()),
    path('myus/', myus),
        path('aroxjakan/list', list_aroxjakanner),
    path('aroxjakan/detail/<int:tt>/<int:տարրիիի>', aroxjakan_details),
    path('aroxjakan/create', AroxjakanCreateAPIView.as_view()),
    path('aroxjakan/', aroxjakan),
        path('kanxargelich/list', list_kanxargelichner),
    path('kanxargelich/detail/<int:jo>/<int:ՏՏՏարիիի>', kanxargelich_details),
    path('kanxargelich/create', KanxargelichCreateAPIView.as_view()),
    path('kanxargelich/', kanxargelich),
        path('atam/list', list_atamnabujakanner),
    path('atam/detail/<int:ok>/<int:Tari>', atamnabujakan_details),
    path('atam/create', AtamnabujakanCreateAPIView.as_view()),
    path('atam/', atam),
        path('patvastum/list', list_kanxapahovner),
    path('patvastum/detail/<int:այդի>/<int:tՏարի>', kanxapahov_details),
    path('patvastum/create', KanxapahovCreateAPIView.as_view()),
    path('patvastum/', kanxapahov),
        path('vichak/list', list_vichakner),
    path('vichak/detail/<int:idi>/<int:tttaaarrriii>', vichak_details),
    path('vichak/create', VichakCreateAPIView.as_view()),
    path('vichak/', Vichak),
        path('anashxatunakutyun/list', list_anashxatakanutyunner),
    path('anashxatunakutyun/detail/<int:ididid>/<int:yyeeaarr>', anashxatakanutyun_details),
    path('anashxatunakutyun/create', AnashxatakanutyunCreateAPIView.as_view()),
    path('anashxatunakutyun/', Anashxatakanutyunnk),
        path(r'', homepage)

]
