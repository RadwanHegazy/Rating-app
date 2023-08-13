from .views import ProductViewSet, StarsView
from django.urls import path, include
from rest_framework.routers import DefaultRouter

routre = DefaultRouter()

routre.register(r'products', ProductViewSet)
routre.register(r'stars',StarsView)


urlpatterns = [
    path('',include(routre.urls))
]