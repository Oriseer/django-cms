from django.shortcuts import render, redirect
from .models import Client
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .forms import *


# Create your views here.
class ClientListView(ListView):
    model = Client
    
class ClientDetailView(DetailView):
    model = Client
    

class ClientUpdateView(UpdateView):
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client:client-list')
    
class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client:client-list')


def client_create(request):
    client_form = ClientForm
    client_file = ClientFilesForm
    if request.method == "POST":
        client_form = ClientForm(request.POST)
        client_files = ClientFilesForm(request.POST, request.FILES)
        files = request.FILES.getlist('documents')
        if client_form.is_valid() and client_files.is_valid():
            client_instance = client_form.save(commit=False)
            client_instance.save()
            for f in files:
                client_files_instance = ClientFiles(documents=f, client=client_instance)
                client_files_instance.save()
                return redirect('/client')
    
    context = {
        'client_form': client_form,
        'client_file': client_file
    }
    return render(request, "client/client_form.html", context)
    

