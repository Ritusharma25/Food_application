from rest_framework import serializers
from .models import Food

class Get_FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('name','description')

class Post_FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ('name','description')