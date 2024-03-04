from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models


# Create your models here.
class CategoryModel(models.Model):
    category_name=models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.category_name

class ProductModel(models.Model):
    name=models.CharField(max_length=200)
    actual_price=models.IntegerField(blank=True)
    our_price=models.IntegerField(blank=True)
    rating_count=models.IntegerField(blank=True)
    review_count=models.IntegerField(blank=True)
    packge_fee=models.CharField(max_length=200)
    description=models.TextField(blank=True)
    delivery=models.IntegerField(blank=True)
    rating=models.FloatField(blank=True)
    category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
    image=models.ImageField()
    size=models.CharField(max_length=200,blank=True)
    warranty=models.IntegerField(blank=True)
    offer=models.IntegerField(null=True)
    stock=models.BooleanField(default=False,blank=True)
    def __str__(self):
        return self.name

class AvailableOffers(models.Model):
    off_head=models.CharField(max_length=200)
    off_des=models.CharField(max_length=500)

class GenderModel(models.Model):
    gender=models.CharField(max_length=100)
    def __str__(self):
        return self.gender

class ProfileModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    mob=models.BigIntegerField(null=True)
    email=models.EmailField()
    gender=models.ForeignKey(GenderModel,on_delete=models.CASCADE,null=True)
    address=models.TextField(null=True)


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE,null=True)
    quantity = models.PositiveIntegerField(default=1)
    price=models.IntegerField(null=True)
    rating=models.FloatField(null=True)
    offer=models.IntegerField(null=True)
    name=models.CharField(max_length=200,null=True)


class InventoryModel(models.Model):
    product = models.OneToOneField(ProductModel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
 

class OrdersModel(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    address=models.TextField()
    quantity=models.IntegerField()