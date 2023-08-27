from django.shortcuts import render, HttpResponse
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import generics, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny


# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def menu(request):
    menu_items = Menu.objects.all()
    return render(request, 'menu.html', {"menu": menu_items})

# @api_view()
# @permission_classes([IsAuthenticated])
# def msg(request):
#     return HttpResponse({"message": "this view is protected"})

class MenuItemsView(generics.ListCreateAPIView):
    permission_classes = [AllowAny]
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer