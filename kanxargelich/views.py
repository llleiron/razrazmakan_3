from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Բուժկանխարգելիչ
from rest_framework import generics


class KanxargelichSerializer(serializers.ModelSerializer):
    class Meta:
        model = Բուժկանխարգելիչ
        fields = '__all__'

class KanxargelichCreateAPIView(generics.CreateAPIView):
    serializer_class = KanxargelichSerializer
    queryset = Բուժկանխարգելիչ.objects.all()

def kanxargelich(request):
    return render(request, 'kanxargelich.html')

@api_view(['GET','POST'])
def list_kanxargelichner(request):
    if request.method == "GET":
        kanxargelichner = Բուժկանխարգելիչ.objects.all()
        serializer = KanxargelichSerializer(kanxargelichner, many=True)
        return Response(serializer.data)
    else:
        serializer = KanxargelichSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def kanxargelich_details(request, jo, ՏՏՏարիիի):
    try:
        kanxargelich = Բուժկանխարգելիչ.objects.get(jo=jo, ՏՏՏարիիի=ՏՏՏարիիի)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = KanxargelichSerializer(kanxargelich)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = KanxargelichSerializer(kanxargelich, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        kanxargelich.delete()
        return Response(status=204)