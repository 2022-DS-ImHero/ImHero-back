from pickletools import read_uint1
from django.shortcuts import render, redirect
from .parser import placeParsing
from .forms import IdeaPostModelForm, CrewPostModelForm
from .models import IdeaPost, CrewPost, Tag

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

def makecrew(request):
    posts = CrewPost.objects.order_by('-created')
    tags = Tag.objects.all()
    return render(request, 'crew.html', {'posts':posts, 'tags':tags})

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.crewpost_set.all()

    return render(request, 'crew.html',{'post_list' : post_list, 'tag' : tag})

def uploadCrew(request):
    if request.method == 'POST':
        form = CrewPostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crew')
    else:
        form = CrewPostModelForm()
    return render(request, 'crewUpload.html', {'form':form})
    
def mypage(request):
    return render(request, 'mypage.html')

def info(request):
    res = placeParsing()

    cnterName = {}
    
    
    for number in range(len(res)):
        cnterName[res[number]['cnterNm']] = res[number]['adr']  # key: cnterNm, value: adr

    return render(request, 'info.html', {'cnterName': cnterName})