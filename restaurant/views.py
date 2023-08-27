from django.shortcuts import render
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_items})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]