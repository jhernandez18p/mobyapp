from import_export import resources,fields
from import_export.widgets import (ForeignKeyWidget, CharWidget, IntegerWidget, DecimalWidget)
from .models import (
    Line,
    SubLine,
    Type,
    Color,
    Provider,
    Department,
    Category,
    Article,
)

class ArticleResource(resources.ModelResource):

    id = fields.Field(
        attribute='id',
        column_name='id',
        widget=IntegerWidget()
    )
    description = fields.Field(
        column_name='art_des',
        attribute='description',
        widget=CharWidget()
    )
    code = fields.Field(
        column_name='co_art',
        attribute='code',
        widget=IntegerWidget()
    )
    line = fields.Field(
        column_name='co_lin',
        attribute='line',
        widget=CharWidget()
    )
    sub_line = fields.Field(
        column_name='co_subl',
        attribute='sub_line',
        widget=CharWidget()
    )
    category = fields.Field(
        column_name='co_cat',
        attribute='category',
        widget=CharWidget()
    )
    provider = fields.Field(
        column_name='co_prov',
        attribute='provider',
        widget=CharWidget()
    )
    color = fields.Field(
        column_name='co_color',
        attribute='color',
        widget=CharWidget()
    )
    ref = fields.Field(
        column_name='ref',
        attribute='ref',
        widget=CharWidget()
    )
    model = fields.Field(
        column_name='modelo',
        attribute='model',
        widget=CharWidget()
    )
    origin = fields.Field(
        column_name='procedenci',
        attribute='origin',
        widget=CharWidget()
    )
    sales_unit = fields.Field(
        column_name='uni_venta',
        attribute='sales_unit',
        widget=CharWidget()
    )
    stock = fields.Field(
        column_name='sstock_act',
        attribute='stock',
        widget=IntegerWidget()
    )
    price_1 = fields.Field(
        column_name='prec_vta1',
        attribute='price_1',
        widget=DecimalWidget()
    )
    price_2 = fields.Field(
        column_name='prec_vta2',
        attribute='price_2',
        widget=DecimalWidget()
    )
    price_3 = fields.Field(
        column_name='prec_vta3',
        attribute='price_3',
        widget=DecimalWidget()
    )
    price_4 = fields.Field(
        column_name='prec_vta4',
        attribute='price_4',
        widget=DecimalWidget()
    )
    price_5 = fields.Field(
        column_name='prec_vta5',
        attribute='price_5',
        widget=DecimalWidget()
    )
    item_type = fields.Field(
        column_name='tipo',
        attribute='item_type',
        widget=CharWidget()
    )
    img = fields.Field(
        column_name='picture',
        attribute='img',
        widget=CharWidget()
    )
    class Meta:
        model = Article
        fields = (
        )
        exclude = (
            'name',
            'updated',
            'created_at',
            'slug',
            'picture',
            'is_shipping_required',
            'department',
            'imported',
        )