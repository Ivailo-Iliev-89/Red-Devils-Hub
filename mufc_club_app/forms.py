from django import forms
from .models import FanMessage


class FanMessageForm(forms.ModelForm):
    class Meta:
        model = FanMessage
        fields = ['name', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name',
                'class': 'form-input'}),

            'message': forms.Textarea(attrs={
                'placeholder': 'Your message to the Red Devils..',
                'class': 'form-textarea'})
        }
