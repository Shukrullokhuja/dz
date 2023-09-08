from django.shortcuts import render
from first_app.models import Check,Cofe,tabels,cold_drinks
# Create your views here.

def start_page(request):
    return render(request,'index.html')

def for_check(request):
    check=Check.objects.all()
    context={'check':check}
    return render(request,'Check.html',context=context)

def for_table(request):
    tabel=tabels.objects.all()
    context={'tabels':tabel}
    return render(request,'Tabels.html',context=context)


def cofe(request):
    cofe = Cofe.objects.all()
    context={'cofe':cofe}
    return render(request,'Cofe.html',context=context)


def for_cold_drinks(request):
    colddrinks = cold_drinks.objects.all
    context={'colddrinks':colddrinks}
    return render(request,'Cold_drinks.html',context=context)



