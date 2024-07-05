from django import forms

class inputform(forms.Form):
    shifts=(('1','morning'),('2','afternoon'),('3','evening'))
    first_name=forms.CharField(label='first name', max_length=20)
    last_name=forms.CharField(label="last name", max_length=20)
    shift=forms.ChoiceField(choices=shifts)
    time_log=forms.TimeField()