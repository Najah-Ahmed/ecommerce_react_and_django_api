from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image_prod = serializers.ImageField(max_length=None, allow_empty_file=True, allow_null=None,
                                        required=False)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price',
                  'image_prod', 'stock', 'is_active', 'category')
