from django.db.models import FloatField, F, Sum
from django.shortcuts import render,get_object_or_404,redirect
from articles.models import Cart,Product

def showCart(request):

    #Show list of cart logic goes here
    listCart = Cart.objects.filter(UserId=request.user)
    listCart.total = 0
    for item in listCart:
        listCart.total = listCart.total + Cart.getPriceUnit(item)

    return render(request, 'cart/index.html', {'cart': listCart})

def addCart(request, id):
    Cart.objects.create(ProductId=Product.objects.get(pk=id),UserId=request.user, amount=1)
    return showCart(request)

def removeCart(request, id):
    Cart.objects.filter(pk=id).delete()
    return redirect('showCart')
# Create your views here.
