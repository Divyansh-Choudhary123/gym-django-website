from django.shortcuts import render
from django.http import HttpResponse
from .models import Abc

# Create your views here.
def index(request):
     return render(request,'index.html',{})


def care(request):
     return render(request,'care.html',{})
def mind(request):
     return render(request,'mind.html',{})
def store(request):
     return render(request,'store.html',{})


def loginData(request):
     name = request.POST.get('name','default')
     product = request.POST.get('product','default')
     email = request.POST.get('email','default')
     address = request.POST.get('address','default')
     phone = request.POST.get('phone','default')
     print (name,product,email,address,phone)

     A = Abc(name=name,product=product,email=email,address=address,phone=phone,)
     A.save()

     return HttpResponse('login data saved succefully......')