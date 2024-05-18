from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
from django.views.generic import DetailView
from django.contrib.auth import login
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def index(request):
    return render(request, 'main/index.html')


def materials(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/materials.html', {'title': 'Страница материалов', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def authors(request):
    return render(request, 'main/authors.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Ошибка! Неверная форма'
    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def material_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'main/material_detail.html', {'title': task.title, 'task': task})
