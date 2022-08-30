from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .forms import ContactForm
from . import models

class HomeView(TemplateView):
    template_name = 'main/home.html'

class AboutUsView(TemplateView):
    template_name = 'main/about us.html'

class ContactUSView(FormView):
    template_name = 'main/contact_form.html'
    form_class = ContactForm
    success_url = '/'

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)

class ProductListView(ListView):
    template_name = 'main/product_list.html'
    paginate_by = 4

    def get_queryset(self):
        tag = self.kwargs['tag']
        self.tag = None
        if tag != "all":
            self.tag = get_object_or_404(
                models.ProductTag, slug=tag
            )
        if self.tag:
            products = models.Product.objects.active().filter(
                tags=self.tag
            )
        else:
            products = models.Product.objects.active()
        return products.order_by("name")

class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'main/product_detail.html'




