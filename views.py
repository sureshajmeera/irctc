from django.http import JsonResponse
from .models import Users, Trains
from .serializers import IrctcSerializer, IRCTCADMINList
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def iList(request):
    if request.method == "GET":
        users = Users.objects.all()
        serializer = IrctcSerializer(users, many=True)
        return JsonResponse({'users': serializer.data})
    
    elif request.method == 'POST':
        serializer = IrctcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


@api_view(['GET', 'PUT', 'DELETE'])
def userDetails(request, id):
    user = get_object_or_404(Users, id=id)
    
    if request.method == "GET":
        serializer = IrctcSerializer(user)
        return JsonResponse({'UserName': serializer.data}, safe=False)
    
    elif request.method == "POST":
        serializer = IrctcSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "PUT":
        users = Users.objects.get(id=id)
        serializer = IrctcSerializer(users , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
def TrainList(request):
    if request.method == "GET":
        trains = Trains.objects.all()
        serializer = IRCTCADMINList(trains, many=True)
        return JsonResponse({"trainsList": serializer.data})
    
    elif request.method == "POST":
        serializer = IRCTCADMINList(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def TrainDetail(request, id):
    train = get_object_or_404(Trains, id=id)
    
    if request.method == "GET":
        serializer = IRCTCADMINList(train)
        return JsonResponse({'train': serializer.data}, safe=False)
    
    elif request.method == "PUT":
        trains = Trains.objects.get(id=id)
        serializer = IRCTCADMINList(trains, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        train.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
