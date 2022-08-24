from pickletools import read_uint1
from django.shortcuts import render
from .parser import placeParsing

def home(request):
    return render(request, 'main.html')

def ideaNote(request):
    return render(request, 'ideaNote.html')
    
def uploadIdea(request):
    return render(request, 'uploadIdea.html')

def mypage(request):
    return render(request, 'mypage.html')

def info(request):
    res = placeParsing()

    cnterName = {}
    
    
    for number in range(len(res)):
        cnterName[res[number]['cnterNm']] = res[number]['adr']  # key: cnterNm, value: adr

    return render(request, 'info.html', {'cnterName': cnterName})