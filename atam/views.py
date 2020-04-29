from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ատամնաբուժական
from rest_framework import generics


class AtamnabujakanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ատամնաբուժական
        fields = '__all__'

class AtamnabujakanCreateAPIView(generics.CreateAPIView):
    serializer_class = AtamnabujakanSerializer
    queryset = Ատամնաբուժական.objects.all()

def atam(request):
    return render(request, 'atam.html')
@api_view(['GET','POST'])
def list_atamnabujakanner(request):
    if request.method == "GET":
        atamnabujakanner = Ատամնաբուժական.objects.all()
        serializer = AtamnabujakanSerializer(atamnabujakanner, many=True)
        return Response(serializer.data)
    else:
        serializer = AtamnabujakanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def atamnabujakan_details(request, ok, Tari):
    try:
        atamnabujakan = Ատամնաբուժական.objects.get(ok=ok, Tari=Tari)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = AtamnabujakanSerializer(atamnabujakan)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = AtamnabujakanSerializer(atamnabujakan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        atamnabujakan.delete()
        return Response(status=204)