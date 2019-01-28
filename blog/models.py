from django.db import models

class Product(models.Model):
    product_text = models.CharField(max_length=200,default='Valve')
    pub_date = models.DateTimeField('date published')
    sn = models.CharField(max_length=64) #sn is serial number
    product_component = models.CharField(max_length=200)
    product_production = models.CharField(max_length=200)
    oee = models.IntegerField(default=0)
    def __str__(self):   # in python2 is __unique__
        return self.product_text

class Maschine(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    maschine_text = models.CharField(max_length=200)
    maschine_ability = models.CharField(max_length=200)
    maschine_component = models.CharField(max_length=200)
    def __str__(self):
        return self.maschine_text

class Componentproduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    component_text_product = models.CharField(max_length=200)
    shapeofproduct = models.CharField(max_length=200)
    product_name = models.CharField(max_length=200)
    production = models.CharField(max_length=200)
    def __str__(self):
        return self.component_text_product

class Componentmaschine(models.Model):
    maschine = models.ForeignKey(Maschine, on_delete=models.CASCADE)
    maschine_text= models.CharField(max_length=200)
    component_text_maschine = models.CharField(max_length=200)
    abilityofmaschine = models.CharField(max_length=200)

    quality = models.IntegerField(default=0)
    plant = models.CharField(max_length=200)
    oee_componentofmaschine = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)

    length_workspace = models.IntegerField(default=0)
    width_workspace = models.IntegerField(default=0)
    height_workspace = models.IntegerField(default=0)
    material_tool = models.CharField(max_length=200)

    def __str__(self):
        return self.component_text_maschine
