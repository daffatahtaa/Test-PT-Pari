from django.urls import path
from . import views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title = "CRUD API",
        default_version = 'V1',
        desc = 'Dokumentasi API CRUD'
    )
)

urlpatterns = [
    path('items/', views.get_items),
    path('items/<int:id>/', views.get_item),
    path('items/create/', views.create_item),
    path('items/<int:id>/update/', views.update_item),
    path('items/<int:id>/delete/', views.delete_item),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
