from django.forms import ModelForm
from django import forms
from products.models import Review


class AddReviewForm(ModelForm):
    star_given = forms.IntegerField(max_value=5, min_value=0)
    class Meta:
        model = Review
        fields = ['comment', 'star_given']


class ReviewUpdateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']