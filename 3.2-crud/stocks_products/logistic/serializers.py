from rest_framework import serializers
from .models import Product, Stock, StockProduct


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:                                                             # настройте сериализатор для склада
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):        
        positions = validated_data.pop('positions')                         # достаем связанные данные для других таблиц
        
        stock = super().create(validated_data)                              # создаем склад по его параметрам
        
        for position in positions:                                          # здесь вам надо заполнить связанные таблицы
            StockProduct.objects.get_or_create(stock=stock, **position)     # в нашем случае: таблицу StockProduct
        return stock                                                        # с помощью списка positions


    def update(self, instance, validated_data):        
        positions = validated_data.pop('positions')                      

        stock = super().update(instance, validated_data)

        for position in positions:
            StockProduct.objects.update_or_create(stock=stock, product=position.get('product'), 
                                                  defaults={'price': position.get('price'), 'quantity': position.get('quantity')})

        return stock
