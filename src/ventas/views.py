from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from src.base.models import Carousel, CarouselImage
from src.services.forms import ServiceForm
from src.ventas.models import Article, Photo, Department, Provider, Brands, Category, Color, Line, SubLine
from src.ventas.forms import PhotoForm


class Home(ListView):
    queryset = ''
    template_name = 'app/products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_URL'] = 'Nuestros productos'
        context['has_newsletter'] = True

        articles = Article.objects.exclude(featured=False)
        if articles.exists():
            context['products'] = articles[:8]
        else:
            articles = Article.objects.all()
            if articles.exists():
                context['products'] = articles[:8]


        products_header_carousel = Carousel.objects.filter(Q(page__name="products") & Q(position_id=1))
        if products_header_carousel.exists():
            context['products_header_carousel'] = True
            
            products_header_carousel_images = CarouselImage.objects.filter(Carousel_id=products_header_carousel[0].id)
            if products_header_carousel_images.exists():
                context['products_header_carousel_images'] = products_header_carousel_images
        
        departments = Department.objects.all()
        if departments.exists():
            context['departments'] = departments[:4]

        brands = Brands.objects.all()
        if brands.exists():
            context['brands'] = brands

        context['url_nav'] = 'productos'
        print(self)
        return context


class ProductsList(ListView):

    model = Article
    template_name = 'app/products_list.html'
    paginate_by = 20

    def get_queryset(self):

        article_list = self.model.objects.all()

        line = ''
        if self.request.GET.get('line'):
            line = int(self.request.GET.get('line'))
            article_list = article_list.filter(line=line)
        
        sub_line = ''
        if self.request.GET.get('sub_line'):
            sub_line = int(self.request.GET.get('sub_line'))
            article_list = article_list.filter(sub_line=sub_line)
        
        category = ''
        if self.request.GET.get('category'):
            category = int(self.request.GET.get('category'))
            article_list = article_list.filter(category=category)
        
        department = ''
        if self.request.GET.get('department'):
            department = int(self.request.GET.get('department'))
            article_list = article_list.filter(department=department)
        
        brand = ''
        if self.request.GET.get('brand'):
            brand = int(self.request.GET.get('brand'))
            article_list = article_list.filter(brand=brand)
        
        color = ''
        if self.request.GET.get('color'):
            color = int(self.request.GET.get('color'))
            article_list = article_list.filter(color=color)
        
        search = ''
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            article_list = article_list.filter(
                Q(name__icontains=search)|
                Q(code__icontains=search)|
                Q(line__name__icontains=search)|
                Q(sub_line__name__icontains=search)|
                Q(category__name__icontains=search)|
                Q(department__name__icontains=search)|
                Q(brand__name__icontains=search)|
                Q(color__name__icontains=search)
            )

        return article_list
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        category = 'cat'
        context = super().get_context_data(**kwargs)

        departments = Department.objects.all()
        if departments.exists():
            context['departments'] = departments.filter(active=True).order_by('name')
        
        categories = Category.objects.all()
        if categories.exists():
            context['categories'] = categories.filter(active=True).order_by('name')
        
        brands = Brands.objects.all()
        if brands.exists():
            context['brands'] = brands.filter(active=True).order_by('name')
        
        colors = Color.objects.all()
        if colors.exists():
            context['colors'] = colors.filter(active=True).order_by('name')
        
        lines = Line.objects.all()
        if lines.exists():
            context['lines'] = lines.filter(active=True).order_by('name')
        
        sub_lines = SubLine.objects.all()
        if sub_lines.exists():
            context['sub_lines'] = sub_lines.filter(active=True).order_by('name')

        url_arg = '&'

        line = ''
        if self.request.GET.get('line'):
            line = lines.get(id=self.request.GET.get('line')).name
            url_arg = '{}line={}&'.format(url_arg,self.request.GET.get('line'))

        sub_line = ''
        if self.request.GET.get('sub_line'):
            sub_line = sub_lines.get(id=self.request.GET.get('sub_line')).name
            url_arg = '{}sub_line={}&'.format(url_arg,self.request.GET.get('sub_line'))

        category = ''
        if self.request.GET.get('category'):
            category = categories.get(id=self.request.GET.get('category')).name
            url_arg = '{}category={}&'.format(url_arg,self.request.GET.get('category'))

        department = ''
        if self.request.GET.get('department'):
            department = departments.get(id=self.request.GET.get('department')).name
            url_arg = '{}department={}&'.format(url_arg,self.request.GET.get('department'))

        brand = ''
        if self.request.GET.get('brand'):
            brand = brands.get(id=self.request.GET.get('brand')).name
            url_arg = '{}brand={}&'.format(url_arg,self.request.GET.get('brand'))

        color = ''
        if self.request.GET.get('color'):
            color = colors.get(id=self.request.GET.get('color')).name
            url_arg = '{}color={}&'.format(url_arg,self.request.GET.get('color'))
        
        search = ''
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            url_arg = '{}search={}&'.format(url_arg,self.request.GET.get('search'))
        
        context['line'] = line
        context['sub_line'] = sub_line
        context['category'] = category
        context['department'] = department
        context['brand'] = brand
        context['color'] = color
        context['search'] = search
        context['url_arg'] = url_arg

        context['SITE_URL'] = 'Departamento %s' % (category)
        context['cat'] = '%s' % (category)
        context['url_nav'] = 'productos'
        return context


class ProductsDetail(DetailView):

    model = Article
    form_class = ServiceForm
    # queryset = ''
    template_name = 'app/detail/product_details.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        object_list = Article.objects.filter(Q(line=context['object'].line) | Q(category=context['object'].category)).order_by('?')
        if object_list.exists():
            context['object_list'] = object_list[:4]

        context['object'].update_counter()
        category = 'herraje'
        form = self.form_class
        context['form'] = form
        context['cat'] = '%s' % (category)
        context['SITE_URL'] = 'Detalle de producto'
        context['url_nav'] = 'productos'
        return context


class Departments(ListView):
    model = Department
    paginate_by = 4
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/departments.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_URL'] = 'Departamentos'

        context['url_nav'] = 'productos'

        return context


class DepartmentDetail(DetailView):

    model = Department
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/detail/departments_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['SITE_URL'] = 'Detalles de Departamentos'
        # context['objects'] = {}
        articles = Article.objects.filter(department=self.get_object().pk)
        if articles.exists():
            context['products'] = articles[:9]
        context['url_nav'] = 'productos'
        return context


class BrandView(ListView):
    model = Brands
    # context_object_name = 'boards'
    paginate_by = 6
    # queryset = ''
    template_name = 'app/providers.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['SITE_URL'] = 'Proveedores'
        # context['objects'] = {}
        context['url_nav'] = 'productos'
        return context


class BrandsDetails(DetailView):
    model = Brands
    # context_object_name = 'boards'
    # queryset = ''
    template_name = 'app/detail/provider_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        articles = Article.objects.filter(provider=self.get_object().pk)
        if articles.exists():
            print()
            context['products'] = articles[:9]
        context['SITE_URL'] = 'Detalles de proveedor'
        # context['objects'] = {}
        context['url_nav'] = 'productos'
        return context