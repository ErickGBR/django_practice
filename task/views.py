from django.shortcuts import render

task = ["foo", "bar", "baz"]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html",{
        "tasks": task,
    })

def add(request):
    return render(request, "tasks/add.html",{})