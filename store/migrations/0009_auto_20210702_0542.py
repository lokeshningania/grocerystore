# Generated by Django 3.1.7 on 2021-07-02 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_product_attributes_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subcategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='store.discount')),
                ('parentcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.categorie')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='store.subcategorie'),
        ),
    ]
