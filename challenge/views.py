from django.shortcuts import render
from .models import ChallengeTag, Professor, Company, Senior
# Create your views here.

def challenge(request):
    p_posts = Professor.objects.order_by('date')
    c_posts = Company.objects.order_by('date')
    s_posts = Senior.objects.order_by('date')
    tags = ChallengeTag.objects.all()
    return render(request, 'challenge.html', {'p_posts':p_posts, 'c_posts':c_posts, 's_posts':s_posts, 'tags':tags})
    


    