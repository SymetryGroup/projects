from django.shortcuts import render
posts =[
    {
    'author': 'YOMISMO' ,
    'title': 'Inicio POST1',
    'content':'Noseah',
    'date':'24 de julio'
},
{

    'author': 'YONOMISMO',
    'title': 'Inicio POST2',
    'content': 'holas',
    'date': '25 de junio'



    }
]
data={
    'titulo':'Todolist',
    'fecha':'30 de junio',
    'desc' :'Pagina de prueba'


}











def home(request):
    context={
        'posts':posts
    }
    return render(request, 'inicio/home.html', context)

def about(request):
    return render(request, 'inicio/about.html', {'title':'about'})


def practica(request):
    context1={
        'data':data
    }
    return render(request, 'inicio/practica.html',context1)