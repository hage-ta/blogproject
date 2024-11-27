from django import forms
from .models import GameTip

class GameTipForm(forms.ModelForm):
    class Meta:
        model = GameTip
        fields = ['title', 'detail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'detail': forms.Textarea(attrs={'class': 'form-control'}),
        }
