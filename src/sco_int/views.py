from django.shortcuts import render
from grafica import *

# Create your views here.
def home_view(request):
    graficaAltura = ani_al_ti()
    graficaPresion = ani_pr_ti()
    graficaTemperatura = ani_te_ti()
    graficaVelocidad = ani_ve_ti()
    graficaAceleracion = ani_ac_ti()
    
    return render(request,'InterfazScorpion.html',{'graficaAltura': graficaAltura, 
                                                   'graficaPresion': graficaPresion,
                                                   'graficaTemperatura': graficaTemperatura,
                                                   'graficaVelocidad': graficaVelocidad,
                                                   'graficaAceleracion': graficaAceleracion,})
