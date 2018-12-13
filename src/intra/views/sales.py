from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic import ListView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from src.ventas.models import Article, Line, SubLine, Color, Brands, Department, Category


"""
Products
"""
@method_decorator(login_required, name='dispatch')
class TopProducts(ListView):
    model = Article
    template_name = 'intra/products.html'
    paginate_by = 10

    def get_queryset(self):
        object_list = self.model.objects.all().filter(featured=True)
        return object_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'top-products'
        context['SITE_URL'] = 'Top Products'
        context['APP'] = 'Products'
        return context


@method_decorator(login_required, name='dispatch')
class Products(ListView):
    model = Article
    template_name = 'intra/products.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'products'
        context['SITE_URL'] = 'Products'
        context['APP'] = 'Products'
        return context


@method_decorator(login_required, name='dispatch')
class ProductCreate(CreateView):
    """
    """
    model = Article
    fields = [
        'code',
        'model',
        'name',
        'origin',
        'sales_unit',
        'ref',
        'description',
        'item_type',
        'line',
        'category',
        'color',
        'department',
        'brand',
        'provider',
        'sub_line',
        'slug',
        'stock',
        'views',
        'picture',
        'price_1',
        'price_2',
        'price_3',
        'price_4',
        'price_5',
        'updated',
        'created_at',
        'img',
        'active',
        'featured',
        'sale',
        'imported',
        'is_shipping_required'
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProductUpdate(UpdateView):
    """
    """
    model = Article
    fields = [
        'code',
        'model',
        'name',
        'origin',
        'sales_unit',
        'ref',
        'description',
        'item_type',
        'line',
        'category',
        'color',
        'department',
        'brand',
        'provider',
        'sub_line',
        'slug',
        'stock',
        'views',
        'picture',
        'price_1',
        'price_2',
        'price_3',
        'price_4',
        'price_5',
        'img',
        'active',
        'featured',
        'sale',
        'imported',
        'is_shipping_required'
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ProductDelete(DeleteView):
    """
    """
    model = Article
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
Lines
"""
@method_decorator(login_required, name='dispatch')
class ProductLines(ListView):
    model = Line
    template_name = 'intra/lines.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'lines'
        context['SITE_URL'] = 'lines'
        context['APP'] = 'Lineas'
        return context


@method_decorator(login_required, name='dispatch')
class LineCreate(CreateView):
    """
    """
    model = Line
    fields = [
        'description',
        'img',
        'name',
        'code',
        'count',
        'active',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class LineUpdate(UpdateView):
    """
    """
    model = Line
    fields = [
        'description',
        'img',
        'name',
        'code',
        'count',
        'active',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class LineDelete(DeleteView):
    """
    """
    model = Line
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
Sub lines
"""
@method_decorator(login_required, name='dispatch')
class ProductSubLines(ListView):
    model = SubLine
    template_name = 'intra/sublines.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'sub-lines'
        context['SITE_URL'] = 'sub-lines'
        context['APP'] = 'Sub-lineas'
        return context


@method_decorator(login_required, name='dispatch')
class SubLineCreate(CreateView):
    """
    """
    model = SubLine
    fields = [
        'description',
        'img',
        'name',
        'code',
        'parent',
        'count',
        'active',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class SubLineUpdate(UpdateView):
    """
    """
    model = SubLine
    fields = [
        'description',
        'img',
        'name',
        'code',
        'parent',
        'count',
        'active',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class SubLineDelete(DeleteView):
    """
    """
    model = SubLine
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
Colors
"""
@method_decorator(login_required, name='dispatch')
class ProductColor(ListView):
    model = Color
    template_name = 'intra/colors.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'colors'
        context['SITE_URL'] = 'colors'
        context['APP'] = 'Colores'
        return context


@method_decorator(login_required, name='dispatch')
class ColorCreate(CreateView):
    """
    """
    model = Color
    fields = [
        'description',
        'hex_code',
        'name',
        'code',
        'count',
        'active',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ColorUpdate(UpdateView):
    """
    """
    model = Color
    fields = [
        'description',
        'hex_code',
        'name',
        'code',
        'count',
        'active',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class ColorDelete(DeleteView):
    """
    """
    model = Color
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


"""
Brands
"""
@method_decorator(login_required, name='dispatch')
class ProductBrand(ListView):
    model = Brands
    template_name = 'intra/brands.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'brands'
        context['SITE_URL'] = 'brands'
        context['APP'] = 'Marcas'
        return context


@method_decorator(login_required, name='dispatch')
class BrandCreate(CreateView):
    """
    """
    model = Brands
    fields = [
        'background',
        'description',
        'img',
        'logo',
        'name',
        'slug',
        'website',
        'code',
        'count',
        'active',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BrandUpdate(UpdateView):
    """
    """
    model = Brands
    fields = [
        'background',
        'description',
        'img',
        'logo',
        'name',
        'slug',
        'website',
        'code',
        'count',
        'active',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class BrandDelete(DeleteView):
    """
    """
    model = Brands
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

"""
Categories
"""
@method_decorator(login_required, name='dispatch')
class ProductCategory(ListView):
    model = Category
    template_name = 'intra/categories.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'categories'
        context['SITE_URL'] = 'categories'
        context['APP'] = 'Categorias'
        return context


@method_decorator(login_required, name='dispatch')
class CategoryCreate(CreateView):
    """
    """
    model = Category
    fields = [
        'background',
        'description',
        'img',
        'name',
        'parent'
        'slug',
        'code',
        'count',
        'active'
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CategoryUpdate(UpdateView):
    """
    """
    model = Category
    fields = [
        'background',
        'description',
        'img',
        'name',
        'parent'
        'slug',
        'code',
        'count',
        'active'
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class CategoryDelete(DeleteView):
    """
    """
    model = Category
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

"""
Departments
"""
@method_decorator(login_required, name='dispatch')
class ProductDepartment(ListView):
    model = Department
    template_name = 'intra/departments.html'
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = 'departments'
        context['SITE_URL'] = 'departments'
        context['APP'] = 'Departamentos'
        return context


@method_decorator(login_required, name='dispatch')
class DepartmentCreate(CreateView):
    """
    """
    model = Department
    fields = [
        'background',
        'description',
        'img',
        'name',
        'slug',
        'code',
        'order',
        'count',
        'active',
    ]
    template_name = 'intra/add.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DepartmentUpdate(UpdateView):
    """
    """
    model = Department
    fields = [
        'background',
        'description',
        'img',
        'name',
        'slug',
        'code',
        'order',
        'count',
        'active',
    ]
    template_name = 'intra/edit.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DepartmentDelete(DeleteView):
    """
    """
    model = Department
    template_name = 'intra/delete.html'
    success_url = '/intra/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

