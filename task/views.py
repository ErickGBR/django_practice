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
    #manipulate show tasks by session user
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.cleaned_data
            task = form.cleaned_data["tasks"]
            #manage task by sessions
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("task:index"))
        
        else:
            return render(request, "task/add.html",{
                "form": form
            })
        
    return render(request, "tasks/add.html",{
        "form": NewTaskForm()
        })