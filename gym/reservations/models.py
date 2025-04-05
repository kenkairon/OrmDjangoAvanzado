from django.db import models

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    birth_date = models.DateField()
    
class SportClass(models.Model):
    name = models.CharField(max_length=100)
    max_capacity = models.PositiveBigIntegerField(default=10)
    
class BookingClass(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sport_class = models.ForeignKey(SportClass, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('client', 'sport_class')

    