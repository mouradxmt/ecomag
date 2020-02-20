"""
Definition of forms.
"""

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _


class addComment(forms.Form):

    title = forms.CharField(max_length=50,
                            label=_("Title"),
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': _('Title')}))
    rating = forms.IntegerField(label=_("Password"),
                                widget=forms.TextInput({
                                    'class': 'form-control',
                                    'placeholder': _('Title')}))