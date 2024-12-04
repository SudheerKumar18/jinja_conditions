from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'name':'sudheer kumar','age':22}
    return render(request,'conditions.html',context=d)
def  aa(request):
    data={'Actor':'alluarjun','Gross':1200}
    return render(request,'conditions.html',context=data)