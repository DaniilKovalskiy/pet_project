from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView

from .models import Product, ProductCategory


class ProductListView(ListView):
    model = Product
    template_name = 'products.html'
    paginate_by = 3
    extra_context = {'categories': ProductCategory.objects.all()}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        paginator = context.get('paginator')
        num_pages = paginator.num_pages
        current_page = context.get('page_obj')
        page_num = current_page.number

        if num_pages <= 5 or page_num <= 3:
            pages = [x for x in range(1, min(num_pages+1, 6))]
        elif page_num > num_pages - 3:
            pages = [x for x in range(num_pages - 4, num_pages + 1)]
        else:
            pages = [x for x in range(page_num - 2, page_num + 3)]

        context.update({
            'pages': pages,
        })

        return context

    def get_queryset(self):
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            category = get_object_or_404(ProductCategory, slug=category_slug)
            return Product.objects.filter(category=category)

        return Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = ProductCategory.objects.all()

        context.update({
            'categories': categories,
        })

        return context


class IndexView(TemplateView):
    template_name = 'index.html'
    title = 'Home'

# class ProductContextMixin(ListView):
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         categories = ProductCategory.objects.all()

#         paginator = context.get('paginator')
#         num_pages = paginator.num_pages
#         current_page = context.get('page_obj')
#         page_num = current_page.number

#         if num_pages <= 5 or page_num <= 3:
#             pages = [x for x in range(1, min(num_pages+1, 6))]
#         elif page_num > num_pages - 3:
#             pages = [x for x in range(num_pages - 4, num_pages + 1)]
#         else:
#             pages = [x for x in range(page_num - 2, page_num + 3)]

#         context.update({
#             'categories': categories,
#             'pages': pages,
#         })

#         return context
