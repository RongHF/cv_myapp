from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'myapp/myapp_home_underdevelopment.html')

def home(request):
    return render(request, 'myapp/myapp_home.html')