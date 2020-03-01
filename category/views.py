from django.shortcuts import render,redirect
from django.http import HttpResponse
#import .models from Category
from .models import Product
# Create your views here.

def all(request):
    context={"title":"Home all","product":Product.objects.all()}
    return render(request,"category/all.html",context)
def create(request):
    return render(request,"category/create.html",{"title":"Home create"})
def edit(request):
    return render(request,"category/edit.html",{"title":"Home edit"})
def delete(request):
    return redirect("cat-home")