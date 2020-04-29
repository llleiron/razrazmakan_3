from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import ԸնդհանուրՏեղեկություններ
# Create your views here.

class YndhanurSerializer(serializers.ModelSerializer):
    class Meta:
        model = ԸնդհանուրՏեղեկություններ
        fields = '__all__'

def cllllient(request):
    return render(request, 'yndhanurtexekutyunner.html')

def clllllient(request):
    return render(request, 'yndhanurtexekutyunnerupdate.html')

@api_view(['GET','POST'])
def list_yndhanurner(request):
    if request.method == "GET":
        yndhanurner = ԸնդհանուրՏեղեկություններ.objects.all()
        serializer = YndhanurSerializer(yndhanurner, many=True)
        return Response(serializer.data)
    else:
        serializer = YndhanurSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def yndhanur_details(request, հհ):
    try:
        yndhanur = ԸնդհանուրՏեղեկություններ.objects.get(հհ=հհ)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = YndhanurSerializer(yndhanur)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = YndhanurSerializer(yndhanur, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        yndhanur.delete()
        return Response(status=204)