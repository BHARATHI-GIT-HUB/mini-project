from rest_framework import serializers
# from base.models import Student
from core.models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"