from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def license(request):
    return render(request, 'license.html', {})