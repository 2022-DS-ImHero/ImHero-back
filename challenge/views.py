from django.shortcuts import render
from .models import ChallengeTag, Professor, Company, Senior
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.

def challenge(request):
    p_posts = Professor.objects.order_by('date')
    c_posts = Company.objects.order_by('date')
    s_posts = Senior.objects.order_by('date')
    tags = ChallengeTag.objects.all()
    return render(request, 'challenge.html', {'p_posts':p_posts, 'c_posts':c_posts, 's_posts':s_posts, 'tags':tags})
    
def p_detail(request, post_id):
    post = get_object_or_404(Professor, pk=post_id)
    tags = ChallengeTag.objects.all()
    return render(request, 'challengeDetail.html', {'post':post, 'tags':tags})

def c_detail(request, post_id):
    post = get_object_or_404(Company, pk=post_id)
    tags = ChallengeTag.objects.all()
    return render(request, 'challengeDetail.html', {'post':post, 'tags':tags})

def s_detail(request, post_id):
    post = get_object_or_404(Senior, pk=post_id)
    tags = ChallengeTag.objects.all()
    return render(request, 'challengeDetail.html', {'post':post, 'tags':tags})
