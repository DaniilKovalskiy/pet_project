from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product, ProductCategory


class ProductContextMixin():
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = ProductCategory.objects.all()

        context.update({
            'categories': categories,
        })
        return context


class ProductListView(ProductContextMixin, ListView):
    model = Product
    template_name = 'products.html'
    paginate_by = 3

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(ProductCategory, slug=category_slug)
            return Product.objects.filter(category=category)
        return Product.objects.all()


class ProductDetailView(ProductContextMixin, DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'


class IndexView(TemplateView):
    template_name = 'index.html'
    title = 'Home'
