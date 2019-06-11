from decimal import Decimal

from django.conf import settings

from shop.models import Effect


class Cart(object):
    def __init__(self, request):
        """
        Initialize the cart.
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Add a product to the cart or update its quantity.
        """
        product_id = str(product.effect_id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'effect_price': str(product.effect_price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # update the session cart
        self.session[settings.CART_SESSION_ID] = self.cart
        # mark the session as "modified" to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        """
        Remove a product from the cart.
        """
        product_id = str(product.effect_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Effect.objects.filter(effect_id__in=product_ids)
        for product in products:
            self.cart[str(product.effect_id)]['product'] = product

        for item in self.cart.values():
            item['effect_price'] = Decimal(item['effect_price'])
            item['total_price'] = item['effect_price'] * item['quantity']
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        # 在 django-shop-tutorial-master/shop/templates/shop/base.html 的 {% with total_items=cart|length %}
        # 會被呼叫
        return sum(item['quantity'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # remove cart from session
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True