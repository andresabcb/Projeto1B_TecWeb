from django.shortcuts import render, redirect
from .models import Note

# dúvidas: o que fazer com o id? preciso pegar ou está implícito?
# descobrir onde o index é chamado

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        note = Note(title = title, content = content, tag = tag) # é um objeto
        note.save() # já gravou no banco de dados

        # ou Note.objects.create(title,content)
        # object só serve para a classe
        return redirect('index')

    else:
        # filter() e get() serão úteis
        # objects está se comunicando com o banco de dados
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request,id):
    if request.method == 'POST':
        # carregar o note do banco de dados
        note = Note.objects.get(id=id)
        note.delete()
    return redirect('index')

# nao utilizada
def delete_confirm():
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        return render(request, 'notes/delete_confirm.html', {'note': note})
    else:
        return redirect('index')

def edit(request, id):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        note = Note.objects.get(id=id)
        note.title = title
        note.content = content
        note.tag = tag
        note.save()
        return redirect('index')
    else:
        note = Note.objects.get(id=id)
        return render(request, 'notes/edit.html', {'note': note})

def tags_list(request):
    if request.method == 'POST':
        return redirect('index')

    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/tags.html', {'notes': all_notes})

def tag(request,tag):
    if request.method == 'POST':
        return redirect('index')
    else:
        tag_notes = Note.objects.filter(tag=tag)
        return render(request, 'notes/tag.html', {'notes': tag_notes, 'tag':tag})