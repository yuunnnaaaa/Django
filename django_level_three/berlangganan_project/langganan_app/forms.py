from django import forms
from langganan_app.models import Customer

class NewPelanggan(forms.ModelForm):
    class Meta():
        model = Customer
        fields ='__all__'