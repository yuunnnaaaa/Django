from django.shortcuts import render
from langganan_app.models import Customer
from langganan_app.forms import NewPelanggan

# Create your views here.
def index(request):
    return render (request, 'langganan_app/index.html')

def customers(request):
    customer_list = Customer.objects.order_by('first_name')
    customer_dict = {'customers':customer_list}
    return render (request, 'langganan_app/customers.html', context=customer_dict)

def pelanggan(request):
    form = NewPelanggan()

    if request.method == 'POST':
        form = NewPelanggan(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return customers(request)
        else:
            print("error : form invalid")

    return render (request, 'langganan_app/langganan.html', {'form':form})
    