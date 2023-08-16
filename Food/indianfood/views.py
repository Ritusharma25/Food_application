from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import Get_FoodSerializer, Post_FoodSerializer
from .models import Food

# Create your views here.
@api_view(['GET'])
def get_food(request):
    food_obj = Food.objects.all()
    slzr =  Get_FoodSerializer(food_obj,many=True)
    return Response(slzr.data)

@api_view(['POST'])
def post_food(request):
    slzr = Post_FoodSerializer(data=request.data)
    if slzr.is_valid():
        slzr.save()
    return Response(slzr.data)
