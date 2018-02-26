# Generated by Django 2.0 on 2018-02-26 15:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0003_auto_20180226_0205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.Category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='article',
            name='color',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.Color', verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='article',
            name='department',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.Department', verbose_name='Departamento'),
        ),
        migrations.AlterField(
            model_name='article',
            name='item_type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.Type', verbose_name='Tipo de articulo'),
        ),
        migrations.AlterField(
            model_name='article',
            name='line',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.Line', verbose_name='Linea'),
        ),
        migrations.AlterField(
            model_name='article',
            name='provider',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.Provider', verbose_name='Proveedor'),
        ),
        migrations.AlterField(
            model_name='article',
            name='sub_line',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ventas.SubLine', verbose_name='Sublinea'),
        ),
    ]
