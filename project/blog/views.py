from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.views import View
from .forms import PostForm, CommentForm, SubscribeForm
from .models import Post, Category, Profile, Comment
from django.db.models import Q


def get_categories():
    cats = Category.objects.all()
    count = cats.count()
    half = count // 2
    first_half = cats[:half]
    second_half = cats[half:]
    return {'cats1': first_half, 'cats2': second_half}


def category(request, c=None):
    cObj = get_object_or_404(Category, name=c)
    posts = Post.objects.filter(category=cObj).order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def index(request):
    posts = Post.objects.all().order_by("-published_date")
    # posts = Post.objects.filter(title__contains="News")
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


def post(request, name=None, id=None):
    post = get_object_or_404(Post, title=name, id=id)
    comments = Comment.objects.filter(post=post).order_by('-published_date')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', name=post.title, id=post.id)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'comment': comments,
        'form': form
    }
    context.update(get_categories())
    return render(request, "blog/post.html", context)


def about(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/about.html', context)


def services(request):
    context = {}
    context.update(get_categories())
    return render(request, 'blog/services.html', context)


def contact(request):
    if request.method == 'POST':
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts')
    else:
        form = SubscribeForm()

    context = {'form': form}
    context.update(get_categories())
    return render(request, "blog/contact.html", context)


def search(request):
    query = request.GET.get('query')
    posts = Post.objects.filter(Q(content__icontains=query) | Q(title__icontains=query))
    # posts = Post.objects.all().order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, 'blog/index.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.published_date = now()
            post.user = request.user
            post.save()
            return index(request)

    form = PostForm()
    context = {'form': form}
    context.update(get_categories())
    return render(request, 'blog/create.html', context)


class MyLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')


@login_required
def profile(request):
    # profile_data = get_object_or_404(User, user=request.user)
    # profile_data = Profile.objects.get(user=request.user)
    # context = {'profile_data': profile_data}
    context = {}
    context.update(get_categories())
    return render(request, 'blog/profile.html', context)
#
# class MyLoginView(View):
#     def get(self, request):
#         login(request)
#         return redirect('index')
