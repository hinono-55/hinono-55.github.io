from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ShopPostForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import ShopPost
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.urls import reverse

@method_decorator(login_required, name='dispatch')
class CreateShopView(CreateView):
    form_class=ShopPostForm
    template_name='post_things.html'
    success_url=reverse_lazy('shop:post_done')

    def form_valid(self, form):
        postdata=form.save(commit=False)
        postdata.user=self.request.user
        postdata.save()
        return super().form_valid(form)
    
class ShopSuccessView(TemplateView):
    template_name='post_success.html'

class IndexView(ListView):
    template_name='index.html'
    queryset=ShopPost.objects.order_by('-posted_at')
    paginate_by=9

class Index2View(ListView):
    template_name='index.html'
    queryset=ShopPost.objects.order_by('-price')
    paginate_by=9

class Index3View(ListView):
    template_name='index.html'
    queryset=ShopPost.objects.order_by('price')
    paginate_by=9


class CategoryView(ListView):
    template_name='index.html'
    paginate_by=9

    def get_queryset(self):
        category_id=self.kwargs['category']
        categories=ShopPost.objects.filter( category=category_id).order_by('-posted_at')
        return categories
    
class UserView(ListView):
    template_name='index.html'
    paginate_by=9
    
    def get_queryset(self):
        user_id=self.kwargs['user']
        user_list=ShopPost.objects.filter(user=user_id).order_by('-posted_at')
        return user_list
    
class DetailView(DetailView):
    template_name='detail.html'
    model=ShopPost

class MypageView(ListView):
    template_name='mypage.html'
    paginate_by=9

    def get_queryset(self):
        queryset=ShopPost.objects.filter(user=self.request.user).order_by('-posted_at')
        return queryset
    
class ShopDeleteView(DeleteView):
    model=ShopPost
    template_name='shop_delete.html'
    success_url=reverse_lazy('shop:mypage')

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
    
class CartPurchaseView(ListView):
    model=ShopPost
    template_name = "cart.html"

    def get_queryset(self):
        return ShopPost.objects.filter(pk=self.kwargs['pk'])