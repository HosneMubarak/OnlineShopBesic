from django.urls import path
from .views import ProductApiListView, ProductDetailApiView, ProductDeleteUpdateApiView, \
    ProductCreateApiView

app_name = 'api'

urlpatterns = [
    path('', ProductApiListView.as_view()), #user who authenticated can see product
    path('new/', ProductCreateApiView.as_view()), #only admin create product
    path('<int:pk>/', ProductDetailApiView.as_view()), # #user who authenticated can see product
    # path('<int:pk>/update/', ProductUpdateApiView.as_view()),
    path('<int:pk>/del_update/', ProductDeleteUpdateApiView.as_view()), # employee can update and admin can delete
]
