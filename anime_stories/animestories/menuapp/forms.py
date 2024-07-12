from django import forms
from django.forms import ModelForm
from .models import booking


class bookingform(ModelForm):
    class Meta:
        model = booking
        fields = ('first_name','last_name','guest_number','comment')
        labels={
            'first_name': '',
            'last_name': '',
            'guest_number': '',
            'comment': '',
        }
        widgets={
            'first_name': forms.TextInput(attrs={'class':'form-control','Placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','Placeholder':'Last Name'}),
            'guest_number': forms.TextInput(attrs={'class':'form-control','Placeholder':'Guest Number'}),
            'comment': forms.TextInput(attrs={'class':'form-control','Placeholder':'Message'}),
        }