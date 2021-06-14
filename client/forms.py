from django.forms import ModelForm
from .models import ClientFiles, Client
from django.forms import ClearableFileInput

class ClientFilesForm(ModelForm):
    
    class Meta:
        model = ClientFiles
        fields = ["documents"]
        widgets = {
            'documents': ClearableFileInput(attrs={'multiple': True}),
        }

class ClientForm(ModelForm):
    
    class Meta:
        model = Client
        fields = '__all__'
