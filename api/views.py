from rest_framework import filters, permissions, viewsets,generics,mixins
from .serializer import ProductSeriailzer, StarSeriailzer
from .models import Product, Star




class ProductViewSet (viewsets.ModelViewSet) :
    queryset =  Product.objects.all()
    serializer_class = ProductSeriailzer
    
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]



class StarsView (viewsets.ModelViewSet) :
    queryset = Star.objects.all()
    serializer_class = StarSeriailzer
    
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

