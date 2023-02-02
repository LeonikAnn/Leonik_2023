from django.shortcuts import render
from .models import Project

# def preview(request):
#     return render(request, 'preview.html')
def project_index(request):
    vse_posti = Project.objects.all() #в переменную собрали все посты из таблицы Project
    context = {
        'vse_posti':vse_posti
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk): #id - первичный ключ конкретного поста

    odin_post = Project.objects.get(pk=pk)
    context = {
        'odin_post':odin_post
    }
    return render(request, 'project_detail.html', context=context)