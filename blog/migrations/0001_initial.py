# Generated by Django 2.1.3 on 2018-11-20 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maschine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maschine_text', models.CharField(max_length=200)),
                ('maschine_ability', models.CharField(max_length=200)),
                ('maschine_component', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_text', models.CharField(default='Valve', max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('product_component', models.CharField(max_length=200)),
                ('product_production', models.CharField(max_length=200)),
                ('sn', models.CharField(max_length=64)),
                ('oee', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='maschine',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Product'),
        ),
    ]