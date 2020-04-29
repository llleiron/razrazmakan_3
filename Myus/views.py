from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ՄյուսՄասնագետներ
from rest_framework import generics


class MyusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ՄյուսՄասնագետներ
        fields = '__all__'

class MyusCreateAPIView(generics.CreateAPIView):
    serializer_class = MyusSerializer
    queryset = ՄյուսՄասնագետներ.objects.all()

def myus(request):
    return render(request, 'myus.html')
@api_view(['GET','POST'])
def list_myusner(request):
    if request.method == "GET":
        myusner = ՄյուսՄասնագետներ.objects.all()
        serializer = MyusSerializer(myusner, many=True)
        return Response(serializer.data)
    else:
        serializer = MyusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def myus_details(request, pa, Տարրի):
    try:
        myus = ՄյուսՄասնագետներ.objects.get(pa=pa, Տարրի=Տարրի)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = MyusSerializer(myus)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = MyusSerializer(myus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        myus.delete()
        return Response(status=204)