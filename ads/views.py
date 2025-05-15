from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ad
from .CategoryHelper import CategoryHelper
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.shortcuts import redirect

class AdListView(ListView):
    model = Ad
    template_name = 'ads/ad_list.html'
    context_object_name = 'ads'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        subcategory = self.request.GET.get('subcategory')

        if category:
            queryset = queryset.filter(category=category)
        if subcategory:
            queryset = queryset.filter(subcategory=subcategory)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_category = self.request.GET.get('category', '')
        context['selected_category'] = selected_category
        context['selected_subcategory'] = self.request.GET.get('subcategory', '')
        context['categories'] = Ad.Category.choices

        context['subcategories'] = CategoryHelper.get_subcategory_choices(selected_category)

        return context

@method_decorator(login_required, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ['title', 'description', 'category', 'subcategory', 'status']
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:ad_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_category = self.request.POST.get('category') or self.request.GET.get('category') or ''
        context['selected_category'] = selected_category
        context['categories'] = Ad.Category.choices

        context['subcategories'] = CategoryHelper.get_subcategory_choices(selected_category)

        return context

@method_decorator(login_required, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ['title', 'description', 'category', 'subcategory', 'status']
    template_name = 'ads/ad_form.html'
    success_url = reverse_lazy('ads:ad_list')

    def get_object(self, queryset=None):
        ad = super().get_object(queryset)
        if ad.user != self.request.user:
            messages.error(self.request, "Ви не можете редагувати чуже оголошення.")
            return redirect('ads:ad_list')
        return ad

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selected_category = (
            self.request.POST.get('category') or 
            self.request.GET.get('category') or 
            self.object.category  # при редагуванні
        )
        context['selected_category'] = selected_category
        context['categories'] = Ad.Category.choices

        context['subcategories'] = CategoryHelper.get_subcategory_choices(selected_category)

        return context

@method_decorator(login_required, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    template_name = 'ads/ad_confirm_delete.html'
    success_url = reverse_lazy('ads:ad_list')
    
    def get_object(self, queryset=None):
        ad = super().get_object(queryset)
        if ad.user != self.request.user:
            messages.error(self.request, "Ви не можете видалити чуже оголошення.")
            return redirect('ads:ad_list')
        return ad

class AdDetailView(DetailView):
    model = Ad
    template_name = 'ads/ad_detail.html'
    context_object_name = 'ad'