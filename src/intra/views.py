from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.views.generic import ListView

class Home(ListView):
    # model =
    # context_object_name = 'boards'
    queryset = ''
    template_name = 'intra/home.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Intra'
        return context
