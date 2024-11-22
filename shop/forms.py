from django.forms import ModelForm
from .models import ShopPost

class ShopPostForm(ModelForm):

    class Meta:
        model=ShopPost
        fields=['category', 'title', 'comment', 'image1', 'image2', 'price']