from import_export import resources,fields
from import_export.widgets import (ForeignKeyWidget, CharWidget, IntegerWidget, DecimalWidget)
from .models import (
    Line,SubLine,Type,Color,Provider,Department,Category,Article,Brands,
)

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
        exclude = ('background','img','name','slug')


class CategoryResource(resources.ModelResource):

    class Meta:
        model = Category
        import_id_fields = ('code',)
        export_order = ('name','code','description')
        fields = ['description','code','name']
        exclude = ('background','img','parent','slug')

    
class ArticleResource(resources.ModelResource):

    class Meta:
        model = Article
        import_id_fields = ('code',)

        export_order = (
            'code','description','line__code','category__description','sub_line',\
            'color__code','ref','model','origin','provider__code',\
            'sales_unit','stock','price_1','price_2','price_3',\
            'price_4','price_5','img',
        )

        fields = [
            'category__description','code','color__code','description',\
            'img','item_type','line__code','model','price_1','price_2','price_3',\
            'price_4','price_5','provider__code','ref','sales_unit','stock','sub_line',
            'origin','img',
        ]

        exclude = (
            'name','updated','created_at','slug','picture',\
            'is_shipping_required','department','imported'
        )
