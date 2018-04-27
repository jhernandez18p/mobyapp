from django.shortcuts import render, redirect

def page_not_found_view(request):
    # my custom page not found view
    template = 'auth/page_not_found_view.html'
    context = {}
    context['error_code'] = "404"
    return render(request,template,context)

def error_view(request):
    # my custom error view
    template = 'auth/error_view.html'
    context = {}
    context['error_code'] = "500"
    return render(request,template,context)

def permission_denied_view(request):
    # my custom permission denied view
    template = 'auth/permission_denied_view.html'
    context = {}
    context['error_code'] = "403"
    return render(request,template,context)

def bad_request_view(request):
    # my custom bad request view
    template = 'auth/bad_request_view.html'
    context = {}
    context['error_code'] = "400"
    return render(request,template,context)