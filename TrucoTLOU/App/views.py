from django.shortcuts import render

# Create your views here.

def Inicio(request):

    return render(request, 'App/Inicio.html')

def NaughtyDog(request):

    return render(request, 'App/NaughtyDog.html')

def Modalidades(request):

    return render(request, 'App/Modalidades.html')

def Clases(request):

    return render(request, 'App/Clases.html')    
