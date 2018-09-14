import traceback

from collections import OrderedDict
from copy import deepcopy

from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db.transaction import TransactionManagementError

from import_export import resources,fields
from import_export.results import Error, Result, RowResult
from import_export.widgets import ForeignKeyWidget, CharWidget, IntegerWidget, DecimalWidget

from .models import Line,SubLine,Type,Color,\
    Provider,Department,Category,Article,Brands

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text


import logging
from logging import NullHandler

class LineResource(resources.ModelResource):
    
    class Meta:
        model = Line
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('img',)


class SubLineResource(resources.ModelResource):

    class Meta:
        model = SubLine
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('img','parent')


class TypeResource(resources.ModelResource):

    class Meta:
        model = Type
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('background','img')


class ColorResource(resources.ModelResource):

    class Meta:
        model = Color
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('hex_code',)


class ProviderResource(resources.ModelResource):

    class Meta:
        model = Provider
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('background','img','logo','slug','website')


class BrandsResource(resources.ModelResource):

    class Meta:
        model = Brands
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('background','img','logo','slug','website')


class DepartmentResource(resources.ModelResource):

    class Meta:
        model = Department
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('background','img','slug')


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('background','img','parent','slug')

    
class ArticleResource(resources.ModelResource):
    
    category = fields.Field(column_name='co_cat',attribute='category',widget=ForeignKeyWidget(Category, 'code'),saves_null_values=True)
    code = fields.Field(column_name='co_art',attribute='code') 
    color = fields.Field(column_name='co_color',attribute='color',widget=ForeignKeyWidget(Color, 'code'),saves_null_values=True)
    description = fields.Field(column_name='art_des',attribute='description')
    img = fields.Field(column_name='imagen',attribute='img')
    item_type = fields.Field(column_name='item_type',attribute='item_type',widget=ForeignKeyWidget(Provider, 'code'),saves_null_values=True)
    line = fields.Field(column_name='co_lin',attribute='line',widget=ForeignKeyWidget(Line, 'code'),saves_null_values=True)
    model = fields.Field(column_name='modelo',attribute='model')
    price_1 = fields.Field(column_name='prec_vta1',attribute='price_1')
    price_2 = fields.Field(column_name='prec_vta2',attribute='price_2')
    price_3 = fields.Field(column_name='prec_vta3',attribute='price_3')
    price_4 = fields.Field(column_name='prec_vta4',attribute='price_4')
    price_5 = fields.Field(column_name='prec_vta5',attribute='price_5')
    provider = fields.Field(column_name='co_prov',attribute='provider',widget=ForeignKeyWidget(Provider, 'code'),saves_null_values=True)
    ref = fields.Field(column_name='ref',attribute='ref')
    sales_unit = fields.Field(column_name='uni_venta',attribute='sales_unit')
    stock = fields.Field(column_name='stock_act',attribute='stock')
    sub_line = fields.Field(column_name='co_subl',attribute='sub_line',widget=ForeignKeyWidget(SubLine, 'code'),saves_null_values=True)

    class Meta:
        model = Article
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('code',)
        fields = (
            'code',
            'description',
            'line',
            'category',
            'sub_line',
            'color',
            'provider',
            'ref',
            'model',
            'sales_unit',
            'stock',
            'price_1',
            'price_2',
            'price_3',
            'price_4',
            'price_5',
            'img',
            'item_type',
        )
        export_order = (
            'code',
            'description',
            'line',
            'category',
            'sub_line',
            'color',
            'provider',
            'ref',
            'model',
            'sales_unit',
            'stock',
            'price_1',
            'price_2',
            'price_3',
            'price_4',
            'price_5',
            'img',
            'item_type',
        )
        exclude = (
            'name','updated','created_at','slug','picture',\
            'is_shipping_required','department','imported','origin'
        )
    
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        data = []
        new_data = []
        for x in dataset._data:
            # print(x[9])
            # new_data.append(x[0])
            '''
                [
                    0 '0615501                       ',
                    1 'DESLIZADOR AJUSTABLE DE 6X17 MM. BLANCO                                                                                 ',
                    2 'INDAUX',
                    3 'FITT  ',
                    4 'FTTING',
                    5 '069   ',
                    6 '                        ',
                    7 '                    ',
                    8 'P00049    ',
                    9 'PZA   ',
                    10 -95,
                    11 0.16,
                    12 0.18,
                    13 0.21,
                    14 0.26,
                    15 0.21,
                    16 None,
                    17 0
                ]
            '''
            co_art = str(x[0]).rstrip() #
            # print('co_art -->', co_art)

            art_des = str(x[1]).rstrip() #
            # print('art_des -->', art_des)

            co_lin = str(x[2]).rstrip() #
            # print('co_lin -->', co_lin)

            co_cat = str(x[3]).rstrip() #
            # print('co_cat -->', co_cat)

            co_subl = str(x[4]).rstrip() #
            # print('co_subl -->', co_subl)

            co_color = str(x[5]).rstrip() #
            try:
                co_color = int(co_color)
            except:                
                co_color = None
            # print('co_color -->', co_color)

            ref = str(x[6]).rstrip() #
            # print('ref -->', ref)

            modelo = str(x[7]).rstrip() #
            # print('modelo -->', modelo)

            co_prov = str(x[8]).rstrip() #
            try:
                co_prov = int(co_prov)
            except:
                co_prov = co_prov
            # print('co_prov -->', co_prov)

            uni_venta = str(x[9]).rstrip() #
            # print('uni_venta -->', uni_venta)

            stock_act = int(x[10]) #
            # print('stock_act -->', stock_act)

            prec_vta1 = int(x[11]) #
            # print('prec_vta1 -->', prec_vta1)

            prec_vta2 = int(x[12]) #
            # print('prec_vta2 -->', prec_vta2)

            prec_vta3 = int(x[13]) #
            # print('prec_vta3 -->', prec_vta3)

            prec_vta4 = int(x[14]) #
            # print('prec_vta4 -->', prec_vta4)

            prec_vta5 = int(x[15]) #
            # print('prec_vta5 -->', prec_vta5)

            imagen = x[16] #
            # print('imagen -->', imagen)

            item_type = int(x[17]) #
            # print('item_type -->', item_type)

            new_data.append(co_art) # 
            new_data.append(art_des) # 
            new_data.append(co_lin) # 
            new_data.append(co_cat) # 
            new_data.append(co_subl) # 
            new_data.append(co_color) # 
            new_data.append(ref) # 
            new_data.append(modelo) # 
            new_data.append(co_prov) # 
            new_data.append(uni_venta) # 
            new_data.append(stock_act) # 
            new_data.append(prec_vta1) # 
            new_data.append(prec_vta2) # 
            new_data.append(prec_vta3) # 
            new_data.append(prec_vta4) # 
            new_data.append(prec_vta5) # 
            new_data.append(imagen) # 
            new_data.append(item_type) # 

            data.append(new_data)

            new_data = []
            co_art = ''
            art_des = ''
            co_lin = ''
            co_cat = ''
            co_subl = ''
            co_color = ''
            ref = ''
            modelo = ''
            co_prov = ''
            uni_venta = ''
            stock_act = ''
            prec_vta1 = ''
            prec_vta2 = ''
            prec_vta3 = ''
            prec_vta4 = ''
            prec_vta5 = ''
            imagen = ''
            item_type = ''
        
        # print(dataset._data)
        dataset._data = data
        # print('-----------------')
        # print(dataset._data)