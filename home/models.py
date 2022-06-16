from pickle import TRUE
from django.db import models
from authentications.models import User
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
# Create your models here.





class Products(models.Model):
    id=models.AutoField(primary_key=True,name="product_id")
    Name=models.CharField( max_length=50)
    description = models.TextField(max_length=1000)
    Category=models.ForeignKey("Category", on_delete=models.CASCADE,null=True)
    price = models.FloatField(default=0,null=True)
    Production_country = models.CharField( max_length=50)
    image = models.ImageField( null= True)
    count_sold =models.IntegerField(default=0,verbose_name=('count sold'))
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
    
    
    def __str__(self):
        return self.Name

class Category(models.Model):
    id=models.AutoField(primary_key=True,name="category_id")
    Name = models.CharField(max_length=25)
    category_products = models.ManyToManyField("Products",related_name="categories")
    
    def __str__(self):
        return self.Name 
   
class Recommended(models.Model):
    id=models.AutoField(primary_key=True,name="recommend_id")
    product_name = models.ForeignKey("Products", on_delete=models.CASCADE) 
    recomended_devices = models.ManyToManyField("Products",related_name="aa") 
    
    def __str__(self):
        return str(self.product_name)
       

class OrderItem(models.Model):
    id=models.AutoField(primary_key=True,name="orderitem_id")
    item = models.ForeignKey("Products", on_delete=models.CASCADE)
    cart = models.ForeignKey("Order", on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default = 1)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.user.username) + " " + str(self.item.Name)

    
class Order(models.Model):
    id=models.AutoField(primary_key=True,name="order_id")
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    items = models.ManyToManyField("OrderItem")
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    profit = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)
    

    
@receiver(pre_save, sender=OrderItem) 
def correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Products.objects.get(product_id=cart_items.item.product_id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    total_cart_items = OrderItem.objects.filter(user = cart_items.user )
    cart = Order.objects.get(order_id = cart_items.cart.order_id)
    cart.User = cart_items.user
    cart.items += cart_items.item
    cart.total_price = cart_items.price
    multiplier = 10 / 100
    cart.profit = (cart.total_price * multiplier)
    cart.save()

# def update_subtotal(self):
#         subtotal = 0
#         items = self.cartitem_set.all()
#         for item in items:
#             subtotal += self.total_price
#         self.subtotal = "%.2f" %(subtotal)
#         self.save()