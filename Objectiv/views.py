from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Օբյեկտիվ
from rest_framework import generics


class ObjectivSerializer(serializers.ModelSerializer):
    class Meta:
        model = Օբյեկտիվ
        fields = '__all__'

class ObjectivCreateAPIView(generics.CreateAPIView):
    serializer_class = ObjectivSerializer
    queryset = Օբյեկտիվ.objects.all()

def indexxx(request):
    return render(request, 'objectiv.html')
@api_view(['GET','POST'])
def list_objectivner(request):
    if request.method == "GET":
        objectivner = Օբյեկտիվ.objects.all()
        serializer = ObjectivSerializer(objectivner, many=True)
        return Response(serializer.data)
    else:
        serializer = ObjectivSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        
        return Response(serializer.errors, status=400)


@api_view(['GET','DELETE','PUT'])
def objectiv_details(request, bb, Տարիիի):
    try:
        objectiv = Օբյեկտիվ.objects.get(bb=bb, Տարիիի=Տարիիի)
    except:
        return Response(status=404)
    
    if request.method == 'GET':
        serializer = ObjectivSerializer(objectiv)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ObjectivSerializer(objectiv, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status = 400)
    elif request.method == 'DELETE':
        objectiv.delete()
        return Response(status=204)