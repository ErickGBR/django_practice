from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


tasks = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    tasks = forms.CharField(label="new task")
    priority = forms.IntegerField(label="Priority", min_value=0, max_value=10)

# Create your views here.
def index(request):
    return render(request, "tasks/index.html",{
        "tasks": tasks,
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            task = form.cleaned_data["tasks"]
            tasks.append(task)
            return HttpResponseRedirect(reverse("task:index"))
        
        else:
            return render(request, "task/add.html",{
                "form": form
            })
        
    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
        })