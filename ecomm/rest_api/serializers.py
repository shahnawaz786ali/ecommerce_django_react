from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("__all__")

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model=Store
        fields=("__all__")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=("__all__")

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductImg
        fields=("__all__")

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields=("__all__")

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=CartItem
        fields=("__all__")

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=FileUpload
        fields=("__all__")

class JoinSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='productId')
    class Meta:
        model = CartItem
        fields = ['id','cartId','productId','quantity','product_details','create_at']