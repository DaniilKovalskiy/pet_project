from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product, ProductCategory


class ProductListView(ListView):
    model = Product
    template_name = 'products_by_category.html'
    paginate_by = 3

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(ProductCategory, slug=category_slug)
            return Product.objects.filter(category=category)
        return Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = ProductCategory.objects.all()
        page_obj = context['page_obj']

        context.update({
            'categories': categories,
            'page_obj': page_obj,
        })

        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'
