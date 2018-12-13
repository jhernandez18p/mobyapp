from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.flatpages.models import FlatPage
from src.blog.models import Post
from src.ventas.models import *
from src.base.models import Site, Carousel, CarouselImage
from src.faq.models import Answer, Question
from src.user.models import Newsletter

@method_decorator(login_required, name='dispatch')
class Home(ListView):
    model = User
    template_name = 'intra/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all().filter(is_public=False)
        products = Article.objects.all()

        if products.exists():
            context['products_len'] = products.count()

        if posts.exists():
            if len(posts)>1:
                context['have_many_posts'] = True
            context['posts'] = posts
            context['post_len'] = len(posts)

        context['menu'] = 'home'
        context['SITE_URL'] = 'Intra'
        context['users_len'] = self.model.objects.count()
        context['APP'] = 'Intra'
        return context


@method_decorator(login_required, name='dispatch')
class Conf(ListView):
    model = Site
    template_name = 'intra/conf.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'conf'
        context['SITE_URL'] = 'Configuraciones'
        context['APP'] = 'Configuraciones'
        return context


@method_decorator(login_required, name='dispatch')
class ConfCreate(CreateView):
    """
    """
    model = Site
    fields = [
        'name',
        'title',
        'description',
        'short_description',
        'url',
        'phone',
        'phone2',
        'email',
        'email2',
        'schedule',
        'schedule2',
        'workday',
        'address',
        'address1',
        'logo',
        'site_img',
        'services_img',
        'products_img',
        'is_undercostruction',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfUpdate(UpdateView):
    """
    """
    model = Site
    fields = [
        'name',
        'title',
        'description',
        'short_description',
        'url',
        'phone',
        'phone2',
        'email',
        'email2',
        'schedule',
        'schedule2',
        'workday',
        'address',
        'address1',
        'logo',
        'site_img',
        'services_img',
        'products_img',
        'is_undercostruction',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfDelete(DeleteView):
    """
    """
    model = Site
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
FAQ
"""
@method_decorator(login_required, name='dispatch')
class ConfFAQS(ListView):
    model = Question
    template_name = 'intra/faqs.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        answers = Answer.objects.all()
        if answers.exists():
            context['answers'] = answers
        
        context['menu'] = 'conf-faqs'
        context['SITE_URL'] = 'Preguntas frecuentes'
        context['APP'] = 'Preguntas frecuentes'
        return context


@method_decorator(login_required, name='dispatch')
class ConfFAQQuestionCreate(CreateView):
    """
    """
    model = Question
    fields = ['title']
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfFAQQuestionUpdate(UpdateView):
    """
    """
    model = Question
    fields = ['title']
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfFAQQuestionDelete(DeleteView):
    """
    """
    model = Question
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfFAQAnswerCreate(CreateView):
    """
    """
    model = Answer
    fields = ['question','text']
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfFAQAnswerUpdate(UpdateView):
    """
    """
    model = Answer
    fields = ['question','text']
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfFAQAnswerDelete(DeleteView):
    """
    """
    model = Answer
    fields = ['question','text']
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
Pages
"""
@method_decorator(login_required, name='dispatch')
class ConfPages(ListView):
    model = FlatPage
    template_name = 'intra/pages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'conf-pages'
        context['SITE_URL'] = 'Páginas'
        context['APP'] = 'Páginas'
        return context


@method_decorator(login_required, name='dispatch')
class ConfPageCreate(CreateView):
    """
    """
    model = FlatPage
    fields = ['url', 'title', 'content', 'sites']
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfPageUpdate(UpdateView):
    """
    """
    model = FlatPage
    fields = ['url', 'title', 'content', 'sites']
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfPageDelete(DeleteView):
    """
    """
    model = FlatPage
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
Carrousels
"""
@method_decorator(login_required, name='dispatch')
class ConfSlides(ListView):
    model = Carousel
    template_name = 'intra/slides.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = CarouselImage.objects.all()
        if images.exists():
            context['images'] = images
            
        context['menu'] = 'conf-slides'
        context['SITE_URL'] = 'Carruseles'
        context['APP'] = 'Carruseles'
        return context


@method_decorator(login_required, name='dispatch')
class ConfSlideCreate(CreateView):
    """
    """
    model = Carousel
    fields = [
        'name',
        'description',
        'page',
        'position'
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfSlideUpdate(UpdateView):
    """
    """
    model = Carousel
    fields = [
        'name',
        'description',
        'page',
        'position'
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfSlideDelete(DeleteView):
    """
    """
    model = Carousel
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfSlideImgCreate(CreateView):
    """
    """
    model = CarouselImage
    fields = [
        'Carousel',
        'image',
        'name',
        'text',
        'call_to_action_url'
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfSlideImgUpdate(UpdateView):
    """
    """
    model = CarouselImage
    fields = [
        'Carousel',
        'image',
        'name',
        'text',
        'call_to_action_url'
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfSlideImgDelete(DeleteView):
    """
    """
    model = CarouselImage
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
Newsletters
"""
@method_decorator(login_required, name='dispatch')
class ConfNewsletters(ListView):
    model = Newsletter
    template_name = 'intra/newsletters.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'conf-newsletters'
        context['SITE_URL'] = 'Boletín informativo'
        context['APP'] = 'Boletín informativo'
        return context


@method_decorator(login_required, name='dispatch')
class ConfNewsletterCreate(CreateView):
    """
    """
    model = Newsletter
    fields = [
        'name',
        'subject',
        'email',
        'message',
        'user',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfNewsletterUpdate(UpdateView):
    """
    """
    model = Newsletter
    fields = [
        'name',
        'subject',
        'email',
        'message',
        'user',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ConfNewsletterDelete(DeleteView):
    """
    """
    model = Newsletter
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)