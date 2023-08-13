from rest_framework import serializers
from .models import Product, Star



class ProductSeriailzer (serializers.ModelSerializer) : 
    class Meta : 
        model = Product
        fields = '__all__'
        read_only_fields = ['averge_starts']
        
class StarSeriailzer (serializers.ModelSerializer) : 
    class Meta : 
        model = Star
        fields = '__all__'