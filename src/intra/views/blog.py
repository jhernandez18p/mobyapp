from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_text, force_bytes
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from src.user.tokens import account_activation_token
from src.blog.models import Post, Comment, Tag
from src.services.models import *
from src.ventas.models import *



@method_decorator(login_required, name='dispatch')
class MyBlog(ListView):
    model = Post
    template_name = 'intra/blog.html'
    paginate_by = 5

    def get_queryset(self):
        object_list = self.model.objects.all().filter(author=self.request.user)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'my-posts'
        context['SITE_URL'] = 'Blog'
        context['APP'] = 'Blog'
        return context


@method_decorator(login_required, name='dispatch')
class Blog(ListView):
    model = Post
    template_name = 'intra/blog.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'blog'
        context['SITE_URL'] = 'Blog'
        context['APP'] = 'Blog'
        return context


@method_decorator(login_required, name='dispatch')
class BlogCreate(CreateView):
    """
    """
    model = Post
    fields = [
        'title',
        'sub_title',
        'text',
        'is_public',
        'draft',
        'read_time',
        'img',
        'background',
        'slug',
        'tag',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BlogUpdate(UpdateView):
    """
    """
    model = Post
    fields = [
        'author',
        'updated_by',
        'title',
        'sub_title',
        'text',
        'is_public',
        'draft',
        'read_time',
        'img',
        'background',
        'slug',
        'tag',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BlogDelete(DeleteView):
    """
    """
    model = Post
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
Comments
"""
@method_decorator(login_required, name='dispatch')
class Comments(ListView):
    model = Comment
    template_name = 'intra/comments.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'comments'
        context['SITE_URL'] = 'Comments'
        context['APP'] = 'Comentarios'
        return context


@method_decorator(login_required, name='dispatch')
class CommentCreate(CreateView):
    """
    """
    model = Comment
    fields = [
        'content',
        'parent',
        'approved',
        'post',
        'content_type',
        'object_id',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CommentUpdate(UpdateView):
    """
    """
    model = Comment
    fields = [
        'author',
        'content',
        'parent',
        'approved',
        'post',
        'content_type',
        'object_id',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
    """
    """
    model = Comment
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

"""
Tags
"""
@method_decorator(login_required, name='dispatch')
class Tags(ListView):
    model = Tag
    template_name = 'intra/tags.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'tag'
        context['SITE_URL'] = 'Tag'
        context['APP'] = 'Etiquetas'
        return context


@method_decorator(login_required, name='dispatch')
class TagCreate(CreateView):
    """
    """
    model = Tag
    fields = [
        'title'
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TagUpdate(UpdateView):
    """
    """
    model = Tag
    fields = [
        'title'
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class TagDelete(DeleteView):
    """
    """
    model = Tag
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)