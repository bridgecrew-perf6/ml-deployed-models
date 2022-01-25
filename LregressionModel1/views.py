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


reg_model = pickle.load(open('admissionRegression.pickle', 'rb'))
scaler = pickle.load(open('ScalerModel.pickle', 'rb'))


def predict(request):
    global reg_model
    if request.method == 'POST':
        form = newForm(request.POST)
        if form.is_valid():
            GREScore = form.cleaned_data['GREScore']
            TofelScore = form.cleaned_data['TofelScore']
            uniRating = form.cleaned_data['uniRating']
            SopScore = form.cleaned_data['SopScore']
            LORScore = form.cleaned_data['LORScore']
            CGPA = form.cleaned_data['CGPA']
            Research = form.cleaned_data['Research']

            data = [GREScore, TofelScore, uniRating,
                    SopScore, LORScore, CGPA, Research]

            data = scaler.transform([data])
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
