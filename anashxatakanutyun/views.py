from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Anashxatakanutyun
from rest_framework import generics


class AnashxatakanutyunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anashxatakanutyun
        fields = '__all__'

class AnashxatakanutyunCreateAPIView(generics.CreateAPIView):
    serializer_class = AnashxatakanutyunSerializer
    queryset = Anashxatakanutyun.objects.all()

def Anashxatakanutyunnk(request):
    return render(request, 'anashxatakanutyun.html')
@api_view(['GET', 'POST'])
def list_anashxatakanutyunner(request):
    if request.method == "GET":
        anashxatakanutyunner = Anashxatakanutyun.objects.all()
        serializer = AnashxatakanutyunSerializer(anashxatakanutyunner, many=True)
        return Response(serializer.data)
    else:
        serializer = AnashxatakanutyunSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def anashxatakanutyun_details(request, ididid, yyeeaarr):
    try:
        fizikakan = Anashxatakanutyun.objects.get(ididid=ididid, yyeeaarr=yyeeaarr)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = AnashxatakanutyunSerializer(fizikakan)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AnashxatakanutyunSerializer(fizikakan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        fizikakan.delete()
        return Response(status=204)