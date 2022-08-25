from pickletools import read_uint1
from django.shortcuts import render, redirect, get_object_or_404
from .parser import placeParsing
from .forms import IdeaPostModelForm, CrewPostModelForm
from .models import IdeaPost, CrewPost, Tag
from django.views.generic import CreateView
from django.urls import reverse
from django.contrib import auth

class CrewPostCreate(CreateView):
    
    template_name = 'crewUpload.html'
    success_url = '/' #1
    form_class = CrewPostModelForm #2
    
    def get_success_url(self):
        return reverse('makecrew')

def home(request):
    return render(request, 'main.html')

def ideaNote(request):
    posts = IdeaPost.objects.order_by('-created')
    if request.method == 'POST':
        form = IdeaPostModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ideaNote')
    else:
        form = IdeaPostModelForm()
    return render(request, 'ideaNote.html', {'posts':posts, 'form':form})

# def uploadIdea(request):
#     if request.method == 'POST':
#         form = IdeaPostModelForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('ideaNote')
#     else:
#         form = IdeaPostModelForm()
#     return render(request, 'uploadIdea.html', {'form':form})

def makecrew(request):
    posts = CrewPost.objects.order_by('-created')
    tags = Tag.objects.all()
    return render(request, 'crew.html', {'posts':posts, 'tags':tags})

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.crewpost_set.all()

    return render(request, 'crew.html',{'post_list' : post_list, 'tag' : tag})


    
# def challenge(request):
#     return render(request,'challenge.html')

def mypage(request):
    return render(request, 'mypage.html')

def info(request):
    res = placeParsing()

    cnterName = {}
    
    for number in range(30):
        cnterName[res[number]['cnterNm']] = res[number]['adr']  # key: cnterNm, value: adr

    return render(request, 'info.html', {'cnterName': cnterName})


def logout(request):
    auth.logout(request)
    return redirect('home')
