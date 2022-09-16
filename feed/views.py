
import imp
from django.shortcuts import render
from .models import Order
from .serializers import OrderSerializer
from django.http import JsonResponse

# Create your views here.


def order_list(request):
    #get all orders
    #serialize them
    #return json
    
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return JsonResponse(serializer.data)