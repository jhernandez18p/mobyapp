from import_export import resources,fields
from import_export.widgets import (ForeignKeyWidget, CharWidget, IntegerWidget, DecimalWidget)
from .models import (
    Line,SubLine,Type,Color,Provider,Department,Category,Article,
)

class ArticleResource(resources.ModelResource):

    id = fields.Field(attribute='id',column_name='id',widget=ForeignKeyWidget('self'))
    category = fields.Field(column_name='co_cat',attribute='category',widget=ForeignKeyWidget(Category))
    code = fields.Field(column_name='co_art',attribute='code',widget=IntegerWidget())
    color = fields.Field(column_name='co_color',attribute='color',widget=ForeignKeyWidget(Color))
    description = fields.Field(column_name='art_des',attribute='description',widget=CharWidget())
    img = fields.Field(column_name='picture',attribute='img',widget=CharWidget())
    item_type = fields.Field(column_name='tipo',attribute='item_type',widget=ForeignKeyWidget(Type))
    line = fields.Field(column_name='co_lin',attribute='line',widget=ForeignKeyWidget(Line))
    model = fields.Field(column_name='modelo',attribute='model',widget=CharWidget())
    origin = fields.Field(column_name='procedenci',attribute='origin',widget=CharWidget())
    price_1 = fields.Field(column_name='prec_vta1',attribute='price_1',widget=DecimalWidget())
    price_2 = fields.Field(column_name='prec_vta2',attribute='price_2',widget=DecimalWidget())
    price_3 = fields.Field(column_name='prec_vta3',attribute='price_3',widget=DecimalWidget())
    price_4 = fields.Field(column_name='prec_vta4',attribute='price_4',widget=DecimalWidget())
    price_5 = fields.Field(column_name='prec_vta5',attribute='price_5',widget=DecimalWidget())
    provider = fields.Field(column_name='co_prov',attribute='provider',widget=ForeignKeyWidget(Provider))
    ref = fields.Field(column_name='ref',attribute='ref',widget=CharWidget())
    sales_unit = fields.Field(column_name='uni_venta',attribute='sales_unit',widget=CharWidget())
    stock = fields.Field(column_name='sstock_act',attribute='stock',widget=IntegerWidget())
    sub_line = fields.Field(column_name='co_subl',attribute='sub_line',widget=ForeignKeyWidget(SubLine))

    class Meta:
        model = Article
        fields = ()
        exclude = ('name','updated','created_at','slug','picture','is_shipping_required','department','imported',)