from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Գանգաթներ
from rest_framework import generics
# Create your views here.

class GangatnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Գանգաթներ
        fields = '__all__'

class GangatnerCreateAPIView(generics.CreateAPIView):
    serializer_class = GangatnerSerializer
    queryset = Գանգաթներ.objects.all()

def gangat(request):
    return render(request, 'gangat.html')
@api_view(['GET','POST'])
def list_gangatner(request):
    if request.method == "GET":
        gangatner = Գանգաթներ.objects.all()
        serializer = GangatnerSerializer(gangatner, many=True)
        return Response(serializer.data)
    else:
        serializer = GangatnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def gangatner_details(request, gg, տարի):
    try:
        gangat = Գանգաթներ.objects.get(gg=gg, տարի=տարի)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = GangatnerSerializer(gangat)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = GangatnerSerializer(gangat, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        gangat.delete()
        return Response(status=204)