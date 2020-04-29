from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse
from .models import Գրանցում
# Create your views here.

class GrancumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Գրանցում
        fields = '__all__'

def client(request):
    return render(request,"Grancum.html")

def cllient(request):
    return render(request, "GrancumList.html")

def clllient(request):
    # query = request.GET.get('id')
    return render(request, 'GrancumUpdate.html')


@api_view(['GET','POST'])
def list_grancumner(request):
    if request.method == "GET":
        grancumner = Գրանցում.objects.all()
        serializer = GrancumSerializer(grancumner, many=True)
        return Response(serializer.data)
    else:
        serializer = GrancumSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def grancum_details(request, id):
    try:
        grancum = Գրանցում.objects.get(id=id)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = GrancumSerializer(grancum)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GrancumSerializer(grancum, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        grancum.delete()
        return Response(status=204)