# Generated by Django 2.1.3 on 2018-12-22 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20181220_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='componentmaschine',
            name='maschine_text',
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
    ]
