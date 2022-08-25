from django.shortcuts import render

# Create your views here.
def challenge(request):
    return render(request, 'challenge.html')