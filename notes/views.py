from django.shortcuts import render
from django.http import HttpResponse
from .forms import NoteForm
from .models import NoteModel

def index(request):
    return render(request,"notes/index.html")

def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            n = NoteModel(title=title,content=content)
            n.save()
            return HttpResponse("Form is working")
    form = NoteForm()
    return render(request,"notes/create.html",{'form':form})
