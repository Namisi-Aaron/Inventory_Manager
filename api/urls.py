from django.urls import path

from . import views

urlpatterns = [
    path("item/<str:pk>/", views.ItemUpdateDeleteView.as_view()),
    path("items/", views.ItemByCategoryView.as_view()),
    path("add-item/", views.AddItemView.as_view()),
    path("states/", views.StatesView.as_view()),
    path("add-state/", views.AddStateView.as_view()),
    path("category/<str:pk>/", views.CategoryUpdateDeleteView.as_view()),
    path("categories/", views.CategoriesView.as_view()),
    path("add-category/", views.AddCategoryView.as_view()),
    path("tags/", views.TagsView.as_view()),
    path("add-tag/", views.AddTagView.as_view()),
]