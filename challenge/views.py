from django.shortcuts import render
from .models import ChallengeTag, Professor, Company, Senior
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CommentForm, ReCommentForm, ComCommentForm, SeCommentForm
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
    comment_form = CommentForm()

    return render(request, 'challengeDetail.html', {'post':post, 'tags':tags, 'comment_form':comment_form})

def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)
    
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Professor, pk=post_id)
        finished_form.user = request.user
        finished_form.save()

    return redirect('p_detail', post_id)

def likes(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Professor, pk=post_id)

        if post.like_users.filter(pk=request.user.pk).exists():
            post.like_users.remove(request.user)
        else:
            post.like_users.add(request.user)
        return redirect('p_detail')
    return redirect('accouts:login')


def c_detail(request, post_id):
    post = get_object_or_404(Company, pk=post_id)
    tags = ChallengeTag.objects.all()

    comment_form = ComCommentForm()
    return render(request, 'challengeDetail.html', {'post':post, 'tags':tags, 'comment_form':comment_form})


def create_comment_com(request, post_id):
    filled_form = CommentForm(request.POST)
    
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Company, pk=post_id)
        finished_form.user = request.user
        finished_form.save()

    return redirect('c_detail', post_id)


def s_detail(request, post_id):
    post = get_object_or_404(Senior, pk=post_id)
    tags = ChallengeTag.objects.all()
    comment_form = ComCommentForm()
    return render(request, 'challengeDetail.html', {'post':post, 'tags':tags, 'comment_form':comment_form})

def create_comment_se(request, post_id):
    filled_form = CommentForm(request.POST)
    
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Senior, pk=post_id)
        finished_form.user = request.user
        finished_form.save()

    return redirect('s_detail', post_id)