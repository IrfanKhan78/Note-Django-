from django.shortcuts import render, redirect

from .models import Note
from .forms import NoteForm

# Create your views here.

trashes = []

def home(request):
    notes = Note.objects.all()

    context = {'notes' : notes}

    return render(request, 'note/home.html', context)

def detail(request, cid):
    details = Note.objects.get(pk=cid)

    context = {'details' : details}

    return render(request, 'note/detail.html', context)


def add(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note:home')
    else:
        form = NoteForm()
    
    context = {'form' : form}
    return render(request, 'note/add.html', context)

    

def delete(request, cid):
    note_to_delete = Note.objects.get(pk=cid)
    trashes.append(note_to_delete)
    note_to_delete.delete()
    return redirect('note:home')

def trash(request):
    return render(request, 'note/trash.html', {
        'trashes' : trashes
    })

def clear(request):
    trashes.clear()
    return redirect('note:home')
