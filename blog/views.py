from django.shortcuts import render, redirect
from .models import Post, Skill
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.contrib import messages
# Create your views here.

@login_required
def home(request):
    context = {
        'skills': Skill.objects.filter(author=request.user)
    }
    return render(request, 'blog/base.html', context)


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/home.html" # naming convention:<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class MyPostsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/mine.html" # naming convention:<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']

class MyTasksView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = "blog/mytasks.html" # naming convention:<app>/<model>_<viewtype>.html
    context_object_name = 'tasks'
    ordering = ['title']

class MySkillsView(LoginRequiredMixin, ListView):
    model = Skill
    template_name = "blog/menu_items.html" # naming convention:<app>/<model>_<viewtype>.html
    context_object_name = 'skills'
    ordering = ['title']

class SkillsCreateView(LoginRequiredMixin, CreateView):
    model = Skill
    fields = ['title']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Your task has been created!')
        return super().form_valid(form)

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content', 'reflections']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Your post has been created!')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content', 'reflections']
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, f'Your post has been updated!')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author



@login_required
def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})