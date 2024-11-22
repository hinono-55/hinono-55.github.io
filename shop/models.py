from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    title=models.CharField(verbose_name='ジャンル', max_length=20)

    def __str__(self):
        return self.title
    
class ShopPost(models.Model):
    user=models.ForeignKey(CustomUser, verbose_name='ユーザー', on_delete=models.CASCADE)
    category=models.ForeignKey(Category, verbose_name='ジャンル', on_delete=models.PROTECT)
    title=models.CharField(verbose_name='タイトル', max_length=200)
    comment=models.TextField(verbose_name='詳細',)
    image1=models.ImageField(verbose_name='イメージ1', upload_to='photos')
    image2=models.ImageField(verbose_name='イメージ2', upload_to='photos', blank=True, null=True)
    posted_at=models.DateTimeField(verbose_name='出品日時', auto_now_add=True)
    price=models.FloatField(verbose_name='値段',)
    
    def __str__(self):
        return self.title