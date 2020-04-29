from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ծառայություն
from rest_framework import generics


class CarayutyunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ծառայություն
        fields = '__all__'

class CarayutyunCreateAPIView(generics.CreateAPIView):
    serializer_class = CarayutyunSerializer
    queryset = Ծառայություն.objects.all()

def index(request):
    return render(request, 'index.html')
@api_view(['GET','POST'])
def list_carayutyunner(request):
    if request.method == "GET":
        carayutyunner = Ծառայություն.objects.all()
        serializer = CarayutyunSerializer(carayutyunner, many=True)
        return Response(serializer.data)
    else:
        serializer = CarayutyunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def carayutyun_details(request, ll, year):
    try:
        carayutyun = Ծառայություն.objects.get(ll=ll, year=year)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = CarayutyunSerializer(carayutyun)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarayutyunSerializer(carayutyun, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        carayutyun.delete()
        return Response(status=204)