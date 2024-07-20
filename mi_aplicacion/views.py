from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def do(request):
    return render(request, 'do.html')  # Crea este archivo de plantilla si no existe

def portfolio(request):
    return render(request, 'portfolio.html')  # Crea este archivo de plantilla si no existe

def contact(request):
    return render(request, 'contact.html')  # Crea este archivo de plantilla si no existe
