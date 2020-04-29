from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Անամնեզ


class AnamnezSerializer(serializers.ModelSerializer):
    class Meta:
        model = Անամնեզ
        fields = '__all__'

def cllllllient(request):
    return render(request, 'Anamnez.html')

@api_view(['GET','POST'])
def list_anamnez(request):
    if request.method == 'GET':
        anamnezner = Անամնեզ.objects.all()
        serializer = AnamnezSerializer(anamnezner, many=True)
        return Response(serializer.data)
    else:
        serializer = AnamnezSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

@api_view(['GET','DELETE','PUT'])
def anamnez_details(request, ՀՀ):
    try:
        anamnez = Անամնեզ.objects.get(ՀՀ=ՀՀ)
    except:
        return Response(status = 404)
    
    if request.method == 'GET':
        serializer = AnamnezSerializer(anamnez)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AnamnezSerializer(anamnez, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status=400)
    elif request.method == 'DELETE':
        anamnez.delete()
        return Response(status=204)