from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def fun1(request):
    return HttpResponse("succesfully creates")
def home(request):
    return render(request,"home.html")