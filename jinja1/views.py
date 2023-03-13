from django.shortcuts import render

# Create your views here.
def specific_jinjatag(request):
    d={'name':'Mekalasiri','Age':22,'graduation':'BSC(BIOtech)'}
    return render(request,'specific_jinjatag.html',context=d)
