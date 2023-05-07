from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def hello_world(request):
    if request.method == 'POST':
        data = request.POST.get('text')
        print(data)
        message = 'Hello world!'
        print('done')
        return JsonResponse({'message': message})
    else:
        return render(request, "C:/Users/galsa/Desktop/Server_client/myproject/myapp/templates/index.html")
