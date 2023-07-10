from django.contrib import admin
from django.urls import path
from products.views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('category/', ProductListView.as_view(), name='all_products'),
    path('category/<slug:category_slug>/',
         ProductListView.as_view(), name='products_by_category'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail')
]
