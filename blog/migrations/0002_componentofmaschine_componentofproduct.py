# Generated by Django 2.1.3 on 2018-12-19 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Componentofmaschine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_text_maschine', models.CharField(max_length=200)),
                ('typeofmaschine', models.CharField(max_length=200)),
                ('quality', models.IntegerField(default=0)),
                ('oee_componentofmaschine', models.IntegerField(default=0)),
                ('volume', models.IntegerField(default=0)),
                ('shape', models.CharField(max_length=200)),
                ('dr', models.IntegerField(default=0)),
                ('bx', models.IntegerField(default=0)),
                ('feed', models.IntegerField(default=0)),
                ('maschine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Maschine')),
            ],
        ),
        migrations.CreateModel(
            name='Componentofproduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('component_text_product', models.CharField(max_length=200)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Product')),
            ],
        ),
    ]
