from django.shortcuts import render

# Create your views here.
def specific_jinjatag2(request):
    d={'name':'srujana','Age':24,'graduation':'BSC(BioTech)'}
    return render(request,'specific_jinjatag.html',context=d)