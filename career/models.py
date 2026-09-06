from django.db import models
from django.contrib.auth.models import User


class CareerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    target_role = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.target_role}"