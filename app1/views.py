from django.shortcuts import render

# Create your views here.
def ashu(request):
    return render(request,'ashu.html',context={'name':'ashu','age':2})

def nikky(request):
    return render(request, 'nikky.html',context={'name':'nikky','age':8})