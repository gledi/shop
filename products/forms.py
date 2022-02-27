from django import forms

from products.models import Category


class ReviewForm(forms.Form):
    rating = forms.IntegerField(required=True, min_value=1, max_value=5)
    comment = forms.CharField(required=True, widget=forms.Textarea)


class ProductForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    code = forms.CharField(max_length=12, required=True)
    price = forms.DecimalField(decimal_places=2, max_digits=8)
    description = forms.CharField(widget=forms.Textarea)
    picture = forms.FileField(required=True)
    # category_id = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.filter(is_active=True).all()
        choices = [(c.pk, c.name) for c in categories]
        self.fields["category_id"] = forms.ChoiceField(choices=choices)
