from django.shortcuts import render
from . import forms

# Create your views here.

def index(request):
    return render (request, 'basicapp/index.html')

def form_name_view(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            print("Validation success")
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            print(form.cleaned_data['text'])

            
    return render(request, 'basicapp/formpage.html', {'form': form})