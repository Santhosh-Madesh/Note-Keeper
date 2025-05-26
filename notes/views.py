from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NoteForm
from .models import NoteModel

def index(request):
    n = NoteModel.objects.all()
    if n:
        context = []
        for field in n:
            context.append(
                {
                "title":field.title,
                "content":field.content,
                "pk":field.pk,
                }
            )
        return render(request,"notes/index.html",{'context':context})
    return render(request,"notes/index.html")

def create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            n = NoteModel(title=title,content=content)
            n.save()
            return redirect('index')
    form = NoteForm()
    return render(request,"notes/create.html",{'form':form})

def update(request,pk):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            n1 = NoteModel.objects.get(pk=pk)
            n1.delete()
            n2 = NoteModel(title=title,content=content)
            n2.save()
            return redirect('index')
    pk=pk
    n = NoteModel.objects.get(pk=pk)
    title = n.title
    content = n.content
    form = NoteForm(initial={"title":title,"content":content})

    return render(request,"notes/update.html",{'form':form,'pk':pk})

def delete(request,pk):
    n = NoteModel.objects.get(pk=pk)
    n.delete()
    return redirect('index')

def about(request):
    return render(request,"notes/about.html")