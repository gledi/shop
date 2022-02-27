from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(required=True, widget=forms.Textarea)
