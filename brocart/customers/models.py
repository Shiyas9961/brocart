from django.db import models
from django.contrib.auth.models import User
# User Model

class Customer (models.Model) :

    LIVE = 1
    DELETE = 1
    DELETE_CHOICE = ((LIVE, 'Live'), (DELETE, 'Delete'))

    name = models.CharField(max_length = 100)
    address = models.TextField()
    phone = models.CharField(max_length = 20)
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = "customer_profile")
    delete_status = models.IntegerField(choices = DELETE_CHOICE, default = LIVE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self) -> str:
        return self.name