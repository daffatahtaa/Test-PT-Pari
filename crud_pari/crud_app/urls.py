from django.urls import path
from . import views

urlpatters = [
    path('items/', views.get_items),
    path('items/<int:id>/', views.get_item),
    path('items/create/', views.create_item),
    path('items/<int:id>/update/', views.update_item),
    path('items/<int:id>/delete/', views.delete_item),

]