from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from . models import activity
from . form import TodoForm
# Create your views here.


def index(request):
    activity_list = activity.objects.order_by('id')
    form = TodoForm()

    context = {'activities': activity_list, 'form_text': form }
    return render(request, 'todoApp/index.html', context)


@require_POST
def addTodo(request):
    form = TodoForm(request.POST)
    
    if form.is_valid():
        new_todo = activity(text=request.POST['Text'])
        new_todo.save()

    return redirect('index')

 