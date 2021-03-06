# Generated by Django 2.1.3 on 2019-01-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_componentproduct_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentmaschine',
            name='ability_multiaspect',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='accuracy',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='diameter_tool',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='feedspeed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='height_workspace',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='length_tool',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='length_workspace',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='material_tool',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='pressure',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='rotatedspeed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='strock',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='type_tool',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='componentmaschine',
            name='width_workspace',
            field=models.IntegerField(default=0),
        ),
    ]
