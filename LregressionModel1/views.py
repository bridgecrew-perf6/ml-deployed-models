from django import forms, http
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import newForm
from django.template.defaulttags import register
import pickle
from sklearn.preprocessing import StandardScaler


def home(request):
    form = newForm()
    return render(request, 'home.html', {'form': form})


reg_model = pickle.load(open('BostonModel.pickle', 'rb'))
scaler = pickle.load(open('BostonScalerModel.pickle', 'rb'))


def predict(request):
    global reg_model
    if request.method == 'POST':
        form = newForm(request.POST)
        if form.is_valid():
            CRIM = form.cleaned_data['CRIM']
            INDUS = form.cleaned_data['INDUS']
            CHAS = form.cleaned_data['CHAS']
            NOX = form.cleaned_data['NOX']
            RM = form.cleaned_data['RM']
            AGE = form.cleaned_data['AGE']
            DIS = form.cleaned_data['DIS']

            RAD = form.cleaned_data['RAD']
            TAX = form.cleaned_data['TAX']
            PTRATIO = form.cleaned_data['PTRATIO']
            LSTAT = form.cleaned_data['LSTAT']
            B = form.cleaned_data['B']

            data = [CRIM, INDUS, CHAS, NOX, RM, AGE,
                    DIS, RAD, TAX, PTRATIO, B, LSTAT]
            data = scaler.transform([data])
            print(data)
            prediction = format(reg_model.predict(data)[0], '.2f')

            return render(request, 'home.html', {'form': form, 'prediction': prediction})
        else:
            error = form.errors.as_data()
            print(error)

            return render(request, 'home.html', {'message': error, 'form': form})
    return HttpResponse('Please Enter Data From Home Page')


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)[0]
