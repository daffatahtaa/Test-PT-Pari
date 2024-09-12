from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Item
from .serializer import ItemSerializer

@api_view(['GET'])
def get_items(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_item(request, id):
    item = Item.objects.get(id=id)
    serializer = ItemSerializer(item)
    return Response(serializer.data)

@api_view(['POST'])
def create_item(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response (serializer.errors, status=400)

@api_view(['PUT'])
def update_item(request, id):
    item = Item.objects.get(id=id)
    serializer = ItemSerializer(item, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
def delete_item (request, id):
    item = Item.objects.get(id=id)
    item.delete()

    return Response(status=204)
