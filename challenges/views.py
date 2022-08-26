from django.shortcuts import render, get_object_or_404, redirect
from .models import ChallengeTag, Post, Category
from django.views.generic import ListView
from django.urls import reverse
from .forms import CommentForm
# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk'
    paginate_by = 5

    template_name = 'challenge.html'
    success_url = '/' #1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList,self).get_context_data()
        context['categories'] = Category.objects.all()
        # context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

    def get_success_url(self):
        return reverse('challenge')

def challenge(request):
    posts = Post.objects.order_by('date')
    all_category = Category.objects.all()
    return render(request, 'challenge.html', {'posts':posts, 'all_category':all_category})

def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    post_list = category.post_set.all()

    return render(request, 'challenge.html',{'post_list' : post_list, 'category' : category})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    tags = ChallengeTag.objects.all()
    category = Category.objects.all()

    comment_form = CommentForm()

    return render(request, 'challengeDetail.html', {'post':post, 'tags':tags, 'category':category, 'comment_form':comment_form})

def create_comment(request, post_id):
    filled_form = CommentForm(request.POST)

    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.user = request.user
        finished_form.save()

    return redirect('detail', post_id) 