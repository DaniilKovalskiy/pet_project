from django.conf import settings
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from products.views import ProductListView, ProductDetailView, IndexView
from authentication.views import CustomLoginView, UserRegistrationView
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('category/', ProductListView.as_view(), name='all_products'),
    path('category/<slug:category_slug>/',
         ProductListView.as_view(), name='products_by_category'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='authentication/login.html'), name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='registration')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
