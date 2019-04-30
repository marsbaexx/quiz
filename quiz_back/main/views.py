from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.


def index(request):
    return HttpResponse('<h1>Index page</h1>')


def about(request):
    return HttpResponse('<h1>About page</h1>')

def show_product(request, pk):
    return HttpResponse('<h1>{}</h1>'.format(pk))

def current_time(request, num):
    return HttpResponse('<h1>arg number: {}<h2>'.format(num))
   #return HttpResponse('<h1>{}</h1>'.format(datetime.now()))


