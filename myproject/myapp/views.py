from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello_world(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        print(message)
        return HttpResponse("Hello World!")