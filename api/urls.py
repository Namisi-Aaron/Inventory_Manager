from django.urls import path

from . import views

urlpatterns = [
    path("item/<str:pk>/", views.ItemUpdateDeleteView.as_view(), name="item-update-delete"),
    path("items/", views.ItemByCategoryView.as_view(), name="item-filter"),
    path("add-item/", views.AddItemView.as_view(), name="add-item"),
    path("items/<str:pk>/delete/", views.DeleteItemView.as_view(), name="delete-item"),
    path("states/", views.StatesView.as_view()),
    path("add-state/", views.AddStateView.as_view(), name="add-state"),
    path("category/<str:pk>/", views.CategoryUpdateDeleteView.as_view(), name="category-update-delete"),
    path("categories/", views.CategoriesView.as_view()),
    path("add-category/", views.AddCategoryView.as_view(), name="add-category"),
    path("tags/", views.TagsView.as_view()),
    path("add-tag/", views.AddTagView.as_view(), name="add-tag"),
]