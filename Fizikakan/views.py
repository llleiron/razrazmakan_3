from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Ֆիզիկական
from rest_framework import generics


class FizikakanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ֆիզիկական
        fields = '__all__'

class FizikakanCreateAPIView(generics.CreateAPIView):
    serializer_class = FizikakanSerializer
    queryset = Ֆիզիկական.objects.all()

def indexx(request):
    return render(request, 'indexx.html')
@api_view(['GET','POST'])
def list_fizikakanner(request):
    if request.method == "GET":
        fizikakanner = Ֆիզիկական.objects.all()
        serializer = FizikakanSerializer(fizikakanner, many=True)
        return Response(serializer.data)
    else:
        serializer = FizikakanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def fizikakan_details(request, oo, Տարիի):
    try:
        fizikakan = Ֆիզիկական.objects.get(oo=oo, Տարիի=Տարիի)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = FizikakanSerializer(fizikakan)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = FizikakanSerializer(fizikakan, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        fizikakan.delete()
        return Response(status=204)