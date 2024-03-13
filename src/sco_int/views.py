from django.shortcuts import render
from grafica import *

# Create your views here.
def home_view(request):
    graficaAltura = al_ti()
    graficaPresion = pr_ti()
    graficaTemperatura = te_ti()
    graficaVelocidad = ve_ti()
    graficaAceleracion = ac_ti()
    
    return render(request,'InterfazScorpion.html',{'graficaAltura': graficaAltura, 
                                                   'graficaPresion': graficaPresion,
                                                   'graficaTemperatura': graficaTemperatura,
                                                   'graficaVelocidad': graficaVelocidad,
                                                   'graficaAceleracion': graficaAceleracion,})
