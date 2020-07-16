from django import forms
from .models import subscriber

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = subscriber
        fields = '__all__'