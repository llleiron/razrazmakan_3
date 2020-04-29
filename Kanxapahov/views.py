from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Կանխապահով
from rest_framework import generics


class KanxapahovSerializer(serializers.ModelSerializer):
    class Meta:
        model = Կանխապահով
        fields = '__all__'

class KanxapahovCreateAPIView(generics.CreateAPIView):
    serializer_class = KanxapahovSerializer
    queryset = Կանխապահով.objects.all()

def kanxapahov(request):
    return render(request, 'kanxapahov.html')
@api_view(['GET','POST'])
def list_kanxapahovner(request):
    if request.method == "GET":
        patvastumner = Կանխապահով.objects.all()
        serializer = KanxapahovSerializer(patvastumner, many=True)
        return Response(serializer.data)
    else:
        serializer = KanxapahovSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def kanxapahov_details(request, այդի, tՏարի):
    try:
        patvastum = Կանխապահով.objects.get(այդի=այդի, tՏարի=tՏարի)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = KanxapahovSerializer(patvastum)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = KanxapahovSerializer(patvastum, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        patvastum.delete()
        return Response(status=204)