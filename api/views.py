from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import (
    Item,
    Item_State,
    Item_Category,
    Item_Tag
)
from .serializers import (
    ItemSerializer,
    ItemStateSerializer,
    ItemCategorySerializer,
    ItemTagSerializer
)

# Items
class ItemUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class AddItemView(generics.CreateAPIView):
    serializer_class = ItemSerializer    

class ItemByCategoryView(generics.ListAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category', None)
        if category_id:
            return Item.objects.filter(category__id=category_id)
        return Item.objects.all()
    
class DeleteItemView(generics.DestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

# Categories
class CategoriesView(generics.ListAPIView):
    serializer_class = ItemCategorySerializer
    queryset = Item_Category.objects.all()

class AddCategoryView(generics.CreateAPIView):
    serializer_class = ItemCategorySerializer

class CategoryUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item_Category.objects.all()
    serializer_class = ItemCategorySerializer

# States
class StatesView(generics.ListAPIView):
    serializer_class = ItemStateSerializer
    queryset = Item_State.objects.all()


class AddStateView(generics.CreateAPIView):
    serializer_class = ItemStateSerializer

# Tags
class TagsView(generics.ListAPIView):
    serializer_class = ItemTagSerializer
    queryset = Item_Tag.objects.all()

class AddTagView(generics.CreateAPIView):
    serializer_class = ItemTagSerializer