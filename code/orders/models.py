from django.db import models


class Product(models.Model):
    ean = models.CharField(max_length=13)
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name} {self.ean}'


class StockManager(models.Manager):
    def for_product(self, product):
        return self.filter(product=product).get()


class Stock(models.Model):
    product = models.OneToOneField('orders.Product', on_delete=models.CASCADE)
    
    quantity = models.PositiveIntegerField(default=0)
    reserved_quantity = models.PositiveIntegerField(default=0)

    objects = StockManager()

    
class Order(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    product = models.ForeignKey('orders.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

