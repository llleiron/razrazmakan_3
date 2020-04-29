from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Առողջական
from rest_framework import generics


class AroxjakanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Առողջական
        fields = '__all__'

class AroxjakanCreateAPIView(generics.CreateAPIView):
    serializer_class = AroxjakanSerializer
    queryset = Առողջական.objects.all()

def aroxjakan(request):
    return render(request, 'aroxjakan.html')
@api_view(['GET','POST'])
def list_aroxjakanner(request):
    if request.method == "GET":
        aroxjakanner = Առողջական.objects.all()
        serializer = AroxjakanSerializer(aroxjakanner, many=True)
        return Response(serializer.data)
    else:
        serializer = AroxjakanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def aroxjakan_details(request, tt, տարրիիի):
    try:
        aroxjakan = Առողջական.objects.get(tt=tt, տարրիիի=տարրիիի)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = AroxjakanSerializer(aroxjakan)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AroxjakanSerializer(aroxjakan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        aroxjakan.delete()
        return Response(status=204)