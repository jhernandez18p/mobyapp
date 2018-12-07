from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView

from .models import (Post, Comment)
from .forms import CommentForm

class Home(ListView):
    model = Post
    queryset = Post.objects.filter(draft=False)
    # context_object_name = 'boards'
    paginate_by = 6
    template_name = 'app/blog.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Ultimas noticias'
        context['has_newsletter'] = True
        context['url_nav'] = 'blog'

        return context


class BlogDetail(DetailView):

    model = Post
    template_name = 'app/detail/blog_detail.html'
    comments_paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = CommentForm
        context['url_nav'] = 'blog'
        
        comments = Comment.objects.filter(content_type=17, approved=True,object_id=context['object'].id)
        if comments.exists():
            context['has_comments'] = True
            context['comments'] = comments
        else:
            context['has_comments'] = False
        
        page = self.request.GET.get('page')
        comments_paginator = Paginator(comments, self.comments_paginate_by)
        try:
            comments_page_obj = comments_paginator.page(page)
            # context['is_paginated'] = True
        except (PageNotAnInteger, EmptyPage):
            comments_page_obj = comments_paginator.page(1)
        
        context['page_obj'] = comments_page_obj

        return context


@login_required 
def comment_create(request, slug):
    # return HttpResponseRedirect('/blog/%s' % slug)
    #obj = Comment.objects.get(id=id)
    obj = get_object_or_404(Post,slug=slug)

    if obj:
        post = obj
        author = request.user
        _content_type = obj.get_content_type
        object_id = obj.id


        form = CommentForm(request.POST)
    
        if form.is_valid():
            # content_type = ContentType.objects.get(model=_content_type)
            content_data = form.cleaned_data.get("content")

            new_comment = Comment.objects.get_or_create(
                author = request.user,
                content_type= _content_type,
                object_id = object_id,
                content = content_data,
                post = post,
                # parent = parent_obj,
            )
            return HttpResponseRedirect('/blog/%s' % slug)

        else:
            print('invalid')
            return HttpResponseRedirect('/blog/%s' % slug)

    return HttpResponseRedirect('/blog/%s' % slug)


def comment_delete(request, id):
    return HttpResponseRedirect('/')
