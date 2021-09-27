from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        
        note=Note(content=content,title=title)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    if request.method == "POST":
        get_id = request.POST.get('id')
        note = Note.objects.get(id=get_id)
        note.delete()
        return redirect('index')

def update(request,id):
    if request.method=="POST":
        newtitle = request.POST.get('titulo')
        newcontent = request.POST.get('detalhes')
        note = Note.objects.filter(id=id)
        note.update(title=newtitle,content=newcontent)
        return redirect('index')
    else:
        note = Note.objects.get(id = id)
        return render(request, 'notes/index.html', {"note":note})