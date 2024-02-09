from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,unique=True)
    password=models.CharField(max_length=100)
    address=models.CharField(max_length=300)
    phone=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    
class Store(models.Model):
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    title=models.CharField(max_length=200)
    storeId=models.ForeignKey(Store,on_delete=models.CASCADE)
    price=models.IntegerField()
    category=models.CharField(max_length=200)
    stock=models.IntegerField()
    condition=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)

class ProductImg(models.Model):
    productId=models.ForeignKey(Product,on_delete=models.CASCADE)
    url=models.URLField(max_length=200)

class Cart(models.Model):
    userId=models.ForeignKey(User,on_delete=models.CASCADE)
    quantity=models.IntegerField()

class CartItem(models.Model):
    cartId=models.ForeignKey(Cart,on_delete=models.CASCADE)
    productId=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)

def upload_location(instance,filename):
    ext=filename.split(".")[-1]
    return "%/%,%"("img",datetime.now(),ext)

class FileUpload(models.Model):
    cartId=models.ImageField(upload_to=upload_location)