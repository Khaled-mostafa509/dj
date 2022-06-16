from rest_framework import serializers
from .models import Products , Order , OrderItem ,Recommended,Category 

class HomeSerializers(serializers.ModelSerializer):
    # Category=serializers.CharField(source='Category.Name')
    class Meta:
        model = Products
        fields = '__all__'

class CategorySerializers(serializers.ModelSerializer):
    category_products =  HomeSerializers(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id','Name','category_products']
        
class RecommendedSerializers(serializers.ModelSerializer):
    product_name= HomeSerializers( )
    recomended_devices =  HomeSerializers(many=True)
    class Meta:
        model = Recommended
        fields = ['product_name','recomended_devices']

        
class  jsonOrderItem(serializers.ModelSerializer):
    item= serializers.CharField(source='item.Name')
    price= serializers.CharField(source='item.price')
    class Meta:
        model = OrderItem
        fields = ['quantity','item','price']
        
class  jsonOrder(serializers.ModelSerializer):
    # item= serializers.CharField(source='item.Name')
    # price= serializers.CharField(source='item.price')
    # image= serializers.CharField(source='item.image')
    # items= jsonOrderItem(many=True)

    class Meta:
        model = Order
        fields = "__all__"      
        
