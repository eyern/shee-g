from django import forms

from .models import Product
from cart.models import CartItem
from product_app.models import Comments


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['is_gift_wrap']
        # The BooleanField automatically becomes a CheckboxInput widget

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('comment', 'rating')
        widgets = {
            'comment': forms.Textarea(attrs={
                'rows': 3,
                'class': "form-control",
                'placeholder': "Write your comment..."
            }),
            'rating': forms.HiddenInput(),
        }

    def clean_rating(self):
        rating = self.data.get('rating')
        if rating is None or rating == '':
            raise forms.ValidationError('Please select a rating (1–5 stars).')
        try:
            value = int(rating)
        except (TypeError, ValueError):
            raise forms.ValidationError('Invalid rating.')
        if value < 1 or value > 5:
            raise forms.ValidationError('Rating must be between 1 and 5.')
        return value