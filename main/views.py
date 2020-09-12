from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView

from .models import *

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the main index.")

class ProductListView(ListView):
    model = Producto

class ProductDetailView(DetailView):
    model = Producto
