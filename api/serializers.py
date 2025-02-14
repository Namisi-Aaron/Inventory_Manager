from rest_framework import serializers
from base.models import Item, Item_Category, Item_State, Item_Tag

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class ItemCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Category
        fields = '__all__'

class ItemTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Tag
        fields = '__all__'

class ItemStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_State
        fields = '__all__'