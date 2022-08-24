from django.shortcuts import render
from .parser import placeParsing

def info(request):
    res = placeParsing()

    cnterName = {}
    
    
    for number in range(len(res)):
        cnterName[res[number]['cnterNm']] = res[number]['adr']  # key: cnterNm, value: adr

    return render(request, 'info.html', {'cnterName': cnterName})