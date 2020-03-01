from django.db.models import FloatField, F, Sum
from django.shortcuts import render,get_object_or_404
from articles.models import Cart,Product

def showCart(request):

    #Show list of cart logic goes here
    listCart = Cart.objects.filter(UserId=request.user)
    listCart.total = Cart.objects.filter(UserId=request.user).aggregate(Total=Sum(F('amount')))
    return render(request, 'cart/index.html', {'cart': listCart})

def addCart(request, id):
    Cart.objects.create(ProductId=Product.objects.get(pk=id),UserId=request.user, amount=1)
    return showCart(request)

def removeCart(request, id):
    Cart.objects.filter(pk=id).delete()
    return showCart(request)
# Create your views here.
