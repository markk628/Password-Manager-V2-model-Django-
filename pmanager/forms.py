from django import forms
from pmanager.models import Platform


class PlatformForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    model = Platform