from django.urls import path
from .views import product_list, product_detail, ProductUpdateView, ProdcutCreateView, ProductDeleteView

app_name = 'shop'

urlpatterns = [
    path('', product_list, name='product-list'),
    path('new/', ProdcutCreateView.as_view(), name='product-create'),
    path('<int:pk>/', product_detail, name='product-detail'),
    path('<int:pk>/delete', ProductDeleteView.as_view(), name='product-delete'),
    path('<int:pk>/update', ProductUpdateView.as_view(), name='product-update'),
]
