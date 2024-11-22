from django.urls import path
from . import views

app_name='shop'

urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),

    path('decend price/', views.Index2View.as_view(), name='index2'),

    path('ascend price/', views.Index3View.as_view(), name='index3'),

    path('post/', views.CreateShopView.as_view(), name='post'),

    path('post_done/', views.ShopSuccessView.as_view(), name='post_done'),

    path('shops/<int:category>/', views.CategoryView.as_view(), name='shops_cat'),

    path('user-list/<int:user>/', views.UserView.as_view(), name='user_list'),

    path('shop-detail/<int:pk>/', views.DetailView.as_view(), name='shop_detail'),

    path('mypage/', views.MypageView.as_view(), name='mypage'),

    path('shop/<int:pk>/delete/', views.ShopDeleteView.as_view(), name='shop_delete'),

    path('shop-detail/<int:pk>/cart/', views.CartPurchaseView.as_view(), name='cart'),
]