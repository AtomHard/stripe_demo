from django.shortcuts import redirect, render
from main.models import Item
import stripe

stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'


def index(request):
    context = {}
    items = Item.objects.all()
    if items.exists():
        context['items'] = items
    return render(request, 'main/index.html', context=context)


def item_detail(request, itemid):
    context = {}
    item = Item.objects.get(pk=itemid)
    if item:
        context['item'] = item
    return render(request, 'main/item_detail.html', context=context)


def buy_item(request, itemid):
    """
    /create-checkout-session
    При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос
    stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса
    и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму
    stripe.redirectToCheckout(sessionId=session_id)
    """
    item = Item.objects.get(pk=itemid)
    if item:
        session = stripe.checkout.Session.create(

                            line_items=[{
                                'price_data': {
                                    'currency': 'usd',
                                    'product_data': {
                                        'name': item.name,
                                    },
                                    'unit_amount': int(item.price),
                                },
                                'quantity': 1,
                            }],
                            mode="payment",
                            success_url='http://127.0.0.1:8000/success',
                            cancel_url='http://127.0.0.1:8000/cancel',

                        )
        return redirect(session.url, code=303)


def calculate_order_amount(items):
    return items[0].price


def success(request):
    context = {}
    return render(request, 'main/success.html', context=context)


def cancel(request):
    context = {}
    return render(request, 'main/cancel.html', context=context)
