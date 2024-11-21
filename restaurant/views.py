from django.shortcuts import render
from . import serializers, models
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Menu.objects.all()
    serializer_class = serializers.MenuSerializer

class BookingViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer