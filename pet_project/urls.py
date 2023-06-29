from django.contrib import admin
from django.urls import path
from products.views import product_list, ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list),
    path('list/', ProductListView.as_view()),
]
