from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class IHA(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    hourly_wage = models.DecimalField(max_digits=10, decimal_places=2)


class RentedIHA(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    iha = models.ForeignKey(IHA, on_delete=models.CASCADE)
    user_info = models.CharField(max_length=200, blank=True, null=True)
    iha_info = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    wage = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.user_info = f"{self.user.first_name} {self.user.last_name}"
        self.iha_info = f"{self.iha.brand} {self.iha.model}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Rental {self.id} - {self.user.username} - {self.iha.brand} {self.iha.model}"


