from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    name = request.POST.get('name')
    print(name)
    id = request.POST.get('ID')
    print(id)
    return render(request, 'index.html')
    