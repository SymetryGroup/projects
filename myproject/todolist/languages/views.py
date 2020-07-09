from django.shortcuts import render

# Create your views here.

data={
    'titulo':'Ruso'
}


def ruso(request):
    context={
        'data':data
    }
    return render(request,'inicio/ruso.html',context)