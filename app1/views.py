from django.shortcuts import render

# Create your views here.
def g1(request):
    return render(request,'g1.html')
def g2(request):
    return render(request,'g2.html')    