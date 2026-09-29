from django.shortcuts import render

def main(request):
    context = {
        'name': 'Denis',
        'age': 17,
        'city': 'Kyiv',
        'hobby': 'scateboard, cooking, walking'
    }
    return render(request, 'main.html', context)





def projects(request):
    return render(request,'projects.html')




def my_able(request):
    context1 = {
    'bd': 'Навчився працювати з SQLite та pgAdmin',
    'cicle': 'Освоїів цикли While, For',
    'api':'Навчився робити інтегррації через апі'
    }
    return render(request, 'my_able.html', context1)





















# Create your views here.
