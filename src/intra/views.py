from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from src.blog.models import Post, Comment
from src.services.models import *
from src.ventas.models import *

@method_decorator(login_required, name='dispatch')
class Home(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        posts = Post.objects.all().filter(is_public=False)
        if posts.exists():
            if len(posts)>1:
                context['have_many_posts'] = True
            context['posts'] = posts
            context['post_len'] = len(posts)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Intra'
        context['users_len'] = len(users)
        return context


@method_decorator(login_required, name='dispatch')
class Profile(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Perfil de %s' % (self.request.user.username)
        context['APP'] = 'Profile'
        return context


@method_decorator(login_required, name='dispatch')
class Users(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/users.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Intra'
        context['APP'] = 'Users'
        context['ALL_USERS'] = users
        return context


@method_decorator(login_required, name='dispatch')
class Conf(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/conf.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Configuraciones'
        context['APP'] = 'Config'
        return context


@method_decorator(login_required, name='dispatch')
class Blog(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/conf.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Blog'
        context['APP'] = 'Blog'
        return context


@method_decorator(login_required, name='dispatch')
class Products(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/products.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        products = Article.objects.all()
        # Add in a QuerySet of all the books
        if products.exists():
            context['products'] = products
        context['SITE_URL'] = 'Intra'
        context['APP'] = 'Products'
        return context


@method_decorator(login_required, name='dispatch')
class Services(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/services.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Intra'
        context['APP'] = 'Services'
        return context


@method_decorator(login_required, name='dispatch')
class Support(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/support.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Soporte'
        context['APP'] = 'Support'
        return context


@method_decorator(login_required, name='dispatch')
class Medias(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/medias.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Multimedia'
        context['APP'] = 'Medias'
        return context


@method_decorator(login_required, name='dispatch')
class BlogCreate(CreateView):
    """
    """
    model = Blog
    fields = ['']
    queryset = ''
    template = 'intra/add.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BlogUpdate(UpdateView):
    """
    """
    model = Blog
    fields = ['']
    queryset = ''
    template = 'intra/edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BlogDelete(DeleteView):
    """
    """
    model = Blog
    fields = ['']
    queryset = ''
    template = 'intra/delete.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfCreate(CreateView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template = 'intra/add.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfUpdate(UpdateView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template = 'intra/edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfDelete(DeleteView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template = 'intra/delete.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MediaCreate(CreateView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template = 'intra/add.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MediaUpdate(UpdateView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template = 'intra/edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class MediaDelete(DeleteView):
    """
    """
    # model = ''
    fields = ['']
    queryset = ''
    template = 'intra/delete.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserCreate(CreateView):
    """
    """
    model = Profile
    fields = ['']
    queryset = ''
    template = 'intra/add.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserUpdate(UpdateView):
    """
    """
    model = Profile
    fields = ['']
    queryset = ''
    template = 'intra/edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class UserDelete(DeleteView):
    """
    """
    model = Profile
    fields = ['']
    queryset = ''
    template = 'intra/delete.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProductCreate(CreateView):
    """
    """
    model = ''
    fields = ['']
    queryset = ''
    template = 'intra/add.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProductUpdate(UpdateView):
    """
    """
    model = ''
    fields = ['']
    queryset = ''
    template = 'intra/edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProductDelete(DeleteView):
    """
    """
    model = ''
    fields = ['']
    queryset = ''
    template = 'intra/delete.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ServiceCreate(CreateView):
    """
    """
    model = ''
    fields = ['']
    queryset = ''
    template = 'intra/add.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ServiceUpdate(UpdateView):
    """
    """
    model = ''
    fields = ['']
    queryset = ''
    template = 'intra/edit.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ServiceDelete(DeleteView):
    """
    """
    model = ''
    fields = ['']
    queryset = ''
    template = 'intra/delete.html'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


