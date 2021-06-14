from django.db import models

# Create your models here.
class Client(models.Model):
    name=models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    remarks = models.TextField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name


class ClientFiles(models.Model):
    documents = models.FileField(upload_to="documents")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    