from django import forms
from django.forms import fields


class newForm(forms.Form):

    CRIM = forms.FloatField(


        label='CRIM',
        widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'CRIM', 'id': 'form-CRIM'}),


    )

    INDUS = forms.FloatField(

        label='INDUS', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'INDUS', 'id': 'form-INDUS'}))

    CHAS = forms.FloatField(

        label='CHAS', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'CHAS', 'id': 'form-CHAS'}))

    NOX = forms.FloatField(

        label='NOX', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'NOX', 'id': 'form-NOX'}))

    RM = forms.FloatField(

        label='RM', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'RM', 'id': 'form-RM'}))

    AGE = forms.FloatField(

        label='AGE', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'AGE', 'id': 'form-AGE'}))
    DIS = forms.FloatField(
        label='DIS', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'DIS', 'id': 'form-DIS'}))

    RAD = forms.FloatField(
        label='RAD', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'RAD', 'id': 'form-RAD'}))
    TAX = forms.FloatField(
        label='TAX', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'TAX', 'id': 'form-TAX'}))
    PTRATIO = forms.FloatField(
        label='PTRATIO', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'PTRATIO', 'id': 'form-PTRATIO'}))
    B = forms.FloatField(
        label='B', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'B', 'id': 'form-B'}))
    LSTAT = forms.FloatField(
        label='LSTAT', widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'LSTAT', 'id': 'form-LSTAT'}))

    # choices = (
    #     (1, 'yes'),
    #     (0, 'no')
    # )
    # Research = forms.ChoiceField(choices=choices, widget=forms.Select(
    #     attrs={'class': 'form-control mb-3', 'id': 'form_research'}))

    class Meta:
        fields = {'GREScore'}
