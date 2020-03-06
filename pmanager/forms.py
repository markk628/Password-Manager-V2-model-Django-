from django import forms
from pmanager.models import Platform


class PlatformForm(forms.ModelForm):
    """ Render and process a form based on the Platform model. """
    class Meta:
        model = Platform
        fields = ['platform', 'username', 'password']