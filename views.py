from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request, 'myapp/myapp_home.html')