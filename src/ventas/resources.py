import traceback

from collections import OrderedDict
from copy import deepcopy

from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.db.transaction import TransactionManagementError

from import_export.results import Error, Result, RowResult
from import_export import resources,fields
from import_export.widgets import ForeignKeyWidget, CharWidget,\
    IntegerWidget, DecimalWidget

from .models import Line,SubLine,Type,Color,\
    Provider,Department,Category,Article,Brands

try:
    from django.utils.encoding import force_text
except ImportError:
    from django.utils.encoding import force_unicode as force_text

# Set default logging handler to avoid "No handler found" warnings.
import logging  # isort:skip
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

    @classmethod
    def get_diff_class(self):
        """
        Returns the class used to display the diff for an imported instance.
        """
        return resources.Diff
    
    def before_import_row(self, row, **kwargs):
        """
        Override to add additional logic. Does nothing by default.
        """
        # print('Before import row')
        # print(row)
        # print('\n\n')
        new_row = dict(row)
        # print(new_row)
        
        try:
            try:
                _type = int(new_row['type'])
                row_type_header = 'type'
            except KeyError:
                _type = int(new_row['item_type'])
                row_type_header = 'item_type'
            try:
                _type>1
            except Exception:
                _type = 1
            _Type = Type.objects.get( Q(id=_type) | Q(name__startswith=_type) )
            _type = _Type
            print(_type)
        except ObjectDoesNotExist: 
            _type = 1
        
        try:
            try:
                _line = str(new_row['co_lin'])
                row_line_header = 'co_lin'
            except KeyError:
                _line = str(new_row['line__code'])
                row_line_header = 'line__code'
            _line = ''.join(_line.split())
            line = Line.objects.get( Q(code__startswith=_line) | Q(name__startswith=_line) )
            _line = line.id
        except ObjectDoesNotExist:
            _line = Line.objects.first().id
            # print('x')
        
        
        try:
            try:
                _cat = str(new_row['co_cat'])
                row_cat_header = 'co_cat'
            except KeyError:
                try:
                    new_row['category__code']
                    _cat = str(new_row['category__code'])
                    row_cat_header = 'category__code'
                except Exception:
                    new_row['category__description']
                    _cat = str(new_row['category__description'])
                    row_cat_header = 'category__description'
            cat = Category.objects.get( Q( code__startswith=_cat ) | Q( name__startswith=_cat ))
            _cat = cat.id
        except ObjectDoesNotExist:
            _cat = ''
        
        try:
            try:
                _sublin = str(new_row['co_subl'])
                row_sublin_header = 'co_subl'
            except KeyError:
                try:
                    _sublin = str(new_row['sub_line__code'])
                    row_sublin_header = 'sub_line__code'
                except Exception:
                    _sublin = str(new_row['sub_line'])
                    row_sublin_header = 'sub_line'
            sublin = SubLine.objects.get( Q( code__startswith=_sublin ) | Q( name__startswith=_sublin ))
            _sublin = sublin.id
        except ObjectDoesNotExist:
            _sublin = ''

        try:
            try:
                _color = str(new_row['co_color'])
                row_color_header = 'co_color'
            except KeyError:
                _color = str(new_row['color__code'])
                row_color_header = 'color__code'
            color = Color.objects.get( Q( code__startswith=_color ) | Q( name__startswith=_color ))
            _color = color.id
        except ObjectDoesNotExist:
            _color = ''

        try:
            try:
                _prov = str(new_row['co_prov'])
                row_prov_header = 'co_prov'
            except KeyError:
                _prov = str(new_row['provider__code'])
                row_prov_header = 'provider__code'
            prov = Provider.objects.get( Q( code__startswith=_prov ) | Q( name__startswith=_prov ))
            _prov = prov.id
        except ObjectDoesNotExist:
            _prov = ''
        
        new_row[row_type_header] = _type
        new_row[row_line_header] = _line
        new_row[row_cat_header] = _cat
        new_row[row_sublin_header] = _sublin
        new_row[row_color_header] = _color
        new_row[row_prov_header] = _prov

        new_row = OrderedDict(new_row)
        # row = new_row
        # print('Import the new row')
        # print(new_row)
        # print('\n')



        return new_row

    def import_row(self, row, instance_loader, using_transactions=True, dry_run=False, **kwargs):
        """
        Imports data from ``tablib.Dataset``. Refer to :doc:`import_workflow`
        for a more complete description of the whole import process.
        :param row: A ``dict`` of the row to import
        :param instance_loader: The instance loader to be used to load the row
        :param using_transactions: If ``using_transactions`` is set, a transaction
            is being used to wrap the import
        :param dry_run: If ``dry_run`` is set, or error occurs, transaction
            will be rolled back.
        """
        # print(row)
        # print('\n\n')
        row_result = self.get_row_result_class()()
        
        try:
            new_row = self.before_import_row(row, **kwargs)
            instance, new = self.get_or_init_instance(instance_loader, new_row)

            self.after_import_instance(instance, new, **kwargs)

            if new:
                row_result.import_type = RowResult.IMPORT_TYPE_NEW
            else:
                row_result.import_type = RowResult.IMPORT_TYPE_UPDATE

            row_result.new_record = new
            original = deepcopy(instance)
            diff = self.get_diff_class()(self, original, new)

            if self.for_delete(new_row, instance):
                
                if new:
                    row_result.import_type = RowResult.IMPORT_TYPE_SKIP
                    diff.compare_with(self, None, dry_run)
                else:
                    row_result.import_type = RowResult.IMPORT_TYPE_DELETE
                    self.delete_instance(instance, using_transactions, dry_run)
                    diff.compare_with(self, None, dry_run)

            else:
                self.import_obj(instance, new_row, dry_run)

                if self.skip_row(instance, original):
                    row_result.import_type = RowResult.IMPORT_TYPE_SKIP
                else:
                    self.save_instance(instance, using_transactions, dry_run)
                    self.save_m2m(instance, new_row, using_transactions, dry_run)
                
                diff.compare_with(self, instance, dry_run)
            
            row_result.diff = diff.as_html()
            # Add object info to RowResult for LogEntry
            if row_result.import_type != RowResult.IMPORT_TYPE_SKIP:

                row_result.object_id = instance.pk
                row_result.object_repr = force_text(instance)

            self.after_import_row(new_row, row_result, **kwargs)

        except Exception as e:
            row_result.import_type = RowResult.IMPORT_TYPE_ERROR

            # There is no point logging a transaction error for each row
            # when only the original error is likely to be relevant
            if not isinstance(e, TransactionManagementError):
                logging.exception(e)
            tb_info = traceback.format_exc()
            row_result.errors.append(self.get_error_result_class()(e, tb_info, row))

        return row_result
        
    class Meta:
        model = Article
        skip_unchanged = True
        report_skipped = True
        import_id_fields = ('code',)
        fields = (
            'code',
            'description',
            'line__code',
            'category__code',
            'sub_line__code',
            'color__code',
            'provider__code',
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
            'item_type__id',
            'origin',
        )
        export_order = (
            'code',
            'description',
            'line__code',
            'category__code',
            'sub_line__code',
            'color__code',
            'provider__code',
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
            'item_type__id',
            'origin',
        )
        exclude = (
            'name','updated','created_at','slug','picture',\
            'is_shipping_required','department','imported'
        )


