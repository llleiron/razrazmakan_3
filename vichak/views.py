from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Վիճակ
from rest_framework import generics


class VichakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Վիճակ
        fields = '__all__'

class VichakCreateAPIView(generics.CreateAPIView):
    serializer_class = VichakSerializer
    queryset = Վիճակ.objects.all()

def Vichak(request):
    return render(request, 'vichak.html')
@api_view(['GET','POST'])
def list_vichakner(request):
    if request.method == "GET":
        vichakner = Վիճակ.objects.all()
        serializer = VichakSerializer(vichakner, many=True)
        return Response(serializer.data)
    else:
        serializer = VichakSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def vichak_details(request, idi, tttaaarrriii):
    try:
        vichak = Վիճակ.objects.get(idi=idi, tttaaarrriii=tttaaarrriii)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = VichakSerializer(vichak)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VichakSerializer(vichak, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        vichak.delete()
        return Response(status=204)