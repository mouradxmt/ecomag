"""
Definition of forms.
"""

from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

from .models import Comment
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class addComment(forms.ModelForm):


    title = forms.CharField(max_length=50,
                            label=_("Title"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': _('Title')}))
    Rating = forms.IntegerField(label=_("Rating"),
                                max_value=5,
                                min_value=0,
                                widget=forms.NumberInput({
                                    'class': 'form-control',
                                    'placeholder': _('Rating')}),
                                validators=[
                                    MaxValueValidator(5),
                                    MinValueValidator(0)
                                ]
                                )
    content = forms.CharField(max_length=200,
                            label=_("Comment"),
                            widget=forms.Textarea({
                                'rows' : 4,
                                'class': 'form-control',
                                'placeholder': _('Comment')}))

    class Meta:
        model = Comment
        fields = ('title', 'Rating', 'content')

    def save(self, commit=True):
        comment = super().save(commit=False)
        if commit:
            comment.save()
        return comment
