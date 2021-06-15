from django.shortcuts import render, redirect
from .models import Client, User
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView, View
from django.urls import reverse_lazy, reverse
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def logout_view(request):
    logout(request)
    return redirect('client:login')

class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'client/login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('client:client-list')
        else:
            messages.warning(request, "Invalid username or password")
        return render(request, 'client/login.html')


class ClientListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Client
    
class ClientDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'
    model = Client
    

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Client
    fields = '__all__'
    success_url = reverse_lazy('client:client-list')
    
class ClientDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Client
    success_url = reverse_lazy('client:client-list')

@login_required
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
    

