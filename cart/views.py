from django.core.serializers import json
from django.db.models import FloatField, F, Sum
from django.http import JsonResponse
import json
from django.shortcuts import render, get_object_or_404, redirect
from articles.models import Cart, Product
from cart.models import Order, OrderItem


def showCart(request):
    # Show list of cart logic goes here
    listCart = Cart.objects.filter(UserId=request.user)
    listCart.total = 0
    for item in listCart:
        listCart.total = listCart.total + Cart.getPriceUnit(item)

    return render(request, 'cart/index.html', {'cart': listCart})


def addCart(request, id):
    Cart.objects.create(ProductId=Product.objects.get(pk=id), UserId=request.user, amount=1)
    return showCart(request)


def removeCart(request, id):
    Cart.objects.filter(pk=id).delete()
    return redirect('showCart')


def paymentComplet(request):
    body = json.loads(request.body)
    print('BODY:', body)
    orderList=body['orderList']
    newOrder = Order.objects.create(
        UserId_id=request.user.id
    )
    for item in orderList:
        OrderItem.objects.create(
            order=newOrder,
            product_id=item['productId'],
            price=item['price'],
            quantity=item['amount']
        )
    # product = Product.objects.get(id=body['productId'])

    #print(body.oderList)
    Cart.objects.filter(UserId=request.user).delete()
    return redirect("showCart")
# Create your views here.
# {
# "orderList":
#   [
#   {"productId":"8","amount":"1"},
#   {"productId":"8","amount":"1"},
#   {"productId":"8","amount":"1"}
#   ]
# }