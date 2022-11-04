from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=400)
    logo = models.CharField(max_length=300)
    slug = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length=400)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Sider(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=400)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    rank = models.IntegerField()

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=400)

    def __str__(self):
        return self.name

STOCK = (('in stock','In Stock'),('out of stock', 'Out Of Stock'))
LABELS = (('hot', 'Hot'), ('new','New'),('sale','Sale'))
class Product(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    discounted_price = models.IntegerField(default = 0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.CharField(max_length=100, choices = STOCK)
    labels = models.CharField(max_length=100, choices = LABELS)

    def __str__(self):
        return self.name

class Reviews(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    post = models.CharField(max_length=300)
    feedback = models.TextField()

    def __str__(self):
        return self.name