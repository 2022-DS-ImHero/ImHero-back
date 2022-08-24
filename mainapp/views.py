from pickletools import read_uint1
from django.shortcuts import render, redirect
from .parser import placeParsing
from .forms import IdeaPostModelForm
from .models import IdeaPost

def home(request):
    return render(request, 'main.html')

def ideaNote(request):
    posts = IdeaPost.objects.order_by('-created')
    return render(request, 'ideaNote.html', {'posts':posts})

def uploadIdea(request):
    if request.method == 'POST':
        form = IdeaPostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ideaNote')
    else:
        form = IdeaPostModelForm()
    return render(request, 'uploadIdea.html', {'form':form})

def mypage(request):
    return render(request, 'mypage.html')

def info(request):
    res = placeParsing()

    cnterName = {}
    
    
    for number in range(len(res)):
        cnterName[res[number]['cnterNm']] = res[number]['adr']  # key: cnterNm, value: adr

    return render(request, 'info.html', {'cnterName': cnterName})