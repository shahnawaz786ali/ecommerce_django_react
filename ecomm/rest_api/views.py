from django.shortcuts import render
from .serializers import *
from .models import *
import os
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics,filters
from rest_framework.parsers import JSONParser
# Create your views here.
@csrf_exempt
def create_user(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        serializer =UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data,status=200)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt 
def login_check(request,email):
    try:
        user=User.objects.filter(email=email)
    except:
        return JsonResponse (status=404)
    if request.method=="GET":
        serializer=UserSerializer(user,many=True)
        return JsonResponse(serializer.data,safe=False)

@csrf_exempt 
def get_user(request,pk):
    try:
        user=User.objects.get(id=pk)
    except:
        return JsonResponse (status=404)
    if request.method=="GET":
        serializer=UserSerializer(user)
        return JsonResponse(serializer.data)
    
@csrf_exempt 
def product_list(request,pk):
    if request.method=="GET":
        products=Product.objects.all().order_by('created_at').reverse()
        serializer=UserSerializer(products,many=True)
        return JsonResponse(serializer.data,safe=False)
        
    elif request.method=="POST":
        data=JSONParser().parse(request)
        serializer-ProductSerializer(data=data,status=200)
        if serializer.is_valid(request):
            serializer.save()
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,status=404)

@csrf_exempt 
def product_by_id(request,pk):
    try:
        product=Product.objects.get(id=pk)
    except:
        return JsonResponse (status=404)
    if request.method=="GET":
        serializer=ProductSerializer(product)
        return JsonResponse(serializer.data)
    
    elif request.method=="PUT":
        data = JSONParser().parse(request)
        serializer = ProductSerializer(product,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=="DELETE":
        product.delete()
        return HttpResponse(status=201)
    
@csrf_exempt 
def product_seller(request,storeId):
    try:
        product=Product.objects.get(id=storeId)
    except:
        return JsonResponse(status=404)
    if request.method=="GET":
        serializer=ProductSerializer(product,many=True)
        return JsonResponse(serializer.data,safe=False)
    
@csrf_exempt 
def productImg_list(request,storeId):
    if request.method=="GET":
        product=ProductImg.objects.all()
        serializer=ProductImgSerializer(product,many=True)
        return JsonResponse(serializer.data,safe=False)
    elif request.method=="POST":
        data=JSONParser().parse(request)
        serializer=ProductImgSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        else:
            return JsonResponse(serializer.errors,status=400)
        
@csrf_exempt 
def productImg_product_id(request,productId):
    try:
        productimg=ProductImg.objects.filter(productId=productId)
    except:
        return JsonResponse(status=404)
    if request.method=="GET":
        serializer=ProductImgSerializer(productimg,many=True)
        return JsonResponse(serializer.data,safe=False)
    
@csrf_exempt 
def productImg_by_id(request,id):
    try:
        productimg=ProductImg.objects.get(pk=id)
    except:
        return JsonResponse(status=404)
    if request.method=="GET":
        serializer=ProductImgSerializer(productimg)
        return JsonResponse(serializer.data)
    elif request.method=="DELETE":
        productimg.delete()
        return HttpResponse(status=201)
    
@csrf_exempt 
def product_by_category(request,category):
    try:
        product=Product.objects.filter(category=category)
    except:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=ProductSerializer(product,many=True)
        return JsonResponse(serializer.data,safe=False)
    
@csrf_exempt 
def cart_list(request):
    try:
        cart=Cart.objects.all()
    except:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=CartSerializer(cart,many=True)
        return JsonResponse(serializer.data)
    
@csrf_exempt 
def cart_by_user(request,userId):
    try:
        cart=Cart.objects.filter(userId=userId)
    except:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=CartSerializer(cart,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    elif request.method=="PUT":
        data=JSONParser().parse(request)
        serializer=CartSerializer(cart,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=="DELETE":
        cart.delete()
        return HttpResponse(status=201)
    
@csrf_exempt 
def cartItem_list(request):
    try:
        cartitem=CartItem.objects.all()
    except:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=CartItemSerializer(cartitem,many=True)
        return JsonResponse(serializer.data)
    
@csrf_exempt 
def cartItem_by_id(request,pk):
    try:
        cartitem=CartItem.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=CartItemSerializer(cartitem)
        return JsonResponse(serializer.data)
    
    elif request.method=="PUT":
        data=JSONParser().parse(request)
        serializer=CartItemSerializer(cartitem,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors,status=400)
    elif request.method=="DELETE":
        cartitem.delete()
        return HttpResponse(status=201)
    
@csrf_exempt 
def cartItem_by_cartId(request,cartId):
    try:
        cartitem=CartItem.objects.filter(cartId=cartId)
    except:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=CartItemSerializer(cartitem,many=True)
        return JsonResponse(serializer.data,safe=False)
    
@csrf_exempt 
def cartItem_detect_same_product(request,cartId,productId):
    try:
        cartitem=CartItem.objects.filter(cartId=cartId).filter(productId=productId)
    except:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=CartItemSerializer(cartitem,many=True)
        return JsonResponse(serializer.data,safe=False)
    
class search_product(generics.ListAPIView):
    search_fields=('title','desciption','category')
    filter_backends=filters.SearchFilter
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

@csrf_exempt 
def create_store(request):
    if request.method=="POST":
        data=JSONParser().parse(request)
        serializer=StoreSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=data,status=201)
        return JsonResponse(serializer.errors,status=400)

@csrf_exempt 
def get_store(request,userId):
    try:
        store=CartItem.objects.filter(userId=userId)
    except:
        return HttpResponse(status=404)
    if request.method=="GET":
        serializer=StoreSerializer(store,many=True)
        return JsonResponse(serializer.data,safe=False)
    
class uploadfile(generics.ListAPIView):
    queryset=FileUpload.objects.all()
    serializer_class=FileUploadSerializer

def delete_file(request,filename):
    if request.method == 'GET':
        ext = filename.split(".")[-1]
        filenamenoExt = filename.replace(f'{ext}',"")
        fileDir = "%s/%s.%s" % ("img",filenamenoExt,ext)
        if os.path.isfile((f'"img"/{filename}')):
            os.remove(fileDir)
            return HttpResponse(f'{filename} deleted')
        return HttpResponse('file not found')

def filter_range_price(request,minprice,maxprice):
    try:
        products = Product.objects.filter(price__range=(minprice,maxprice))
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_min_price(request,minprice):
    try:
        products = Product.objects.filter(price__gte=minprice)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_max_price(request,maxprice):
    try:
        products = Product.objects.filter(price__lte=maxprice)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_rating(request,rating):
    try:
        products = Product.objects.filter(rating__gte=rating)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_condition(request,condition):
    try:
        products = Product.objects.filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_price_and_rating(request,minprice,maxprice,rating):
    try:
        products = Product.objects.filter(price__range=(minprice,maxprice)).filter(rating__gte=rating)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_price_and_condition(request,minprice,maxprice,condition):
    products = Product.objects.filter(price__range=(minprice, maxprice)).filter(condition=condition)
    try:
        products = Product.objects.filter(price__range=(minprice,maxprice)).filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_rating_and_condition(request,rating,condition):
    try:
        products = Product.objects.filter(rating__gte=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

def filter_all(request,minprice,maxprice,rating,condition):
    try:
        products = Product.objects.filter(price__range=(minprice,maxprice)).filter(rating__gte=rating).filter(condition=condition)
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)


def get_cart_item_by_cart_id(request,cartId):
    try:
        cartItem = CartItem.objects.filter(cartId_id=cartId).prefetch_related('productId').order_by('create_at')
    except:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = JoinSerializer(cartItem, many=True)
        return JsonResponse(serializer.data, safe=False)