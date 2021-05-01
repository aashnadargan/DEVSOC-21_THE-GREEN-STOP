from django.db import models
from .category import Category

class Product(models.Model):
    name = models.CharField(max_length=50)
    point = models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=4)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();

    @staticmethod
    def get_all_products_by_name(name):
        if name:
            return Product.objects.filter(name__in = name)
        else:
            return Product.get_all_products();


    