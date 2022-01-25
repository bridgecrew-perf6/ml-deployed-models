from django import forms
from django.forms import fields


class newForm(forms.Form):

    GREScore = forms.FloatField(
        max_value=340,

        label='GREScore',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'GREScore', 'id': 'form-GREScore'}),


    )

    TofelScore = forms.FloatField(

        label='TofelScore', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'TofelScore', 'id': 'form-TofelScore'}))

    uniRating = forms.FloatField(
        min_value=0.0,
        max_value=5.0,
        label='uniRating', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'uni Rating', 'id': 'form-uniRating'}))

    SopScore = forms.FloatField(
        min_value=0,
        max_value=5,
        label='SopScore', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'SopScore', 'id': 'form-SopScore'}))

    LORScore = forms.FloatField(
        min_value=1,
        max_value=5,
        label='LORScore', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'LORScore', 'id': 'form-LORScore'}))

    CGPA = forms.FloatField(
        min_value=0,
        max_value=10,
        label='CGPA', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'CGPA', 'id': 'form-CGPA'}))

    choices = (
        (1, 'yes'),
        (0, 'no')
    )
    Research = forms.ChoiceField(choices=choices, widget=forms.Select(
        attrs={'class': 'form-control mb-3', 'id': 'form_research'}))

    class Meta:
        fields = {'GREScore'}
