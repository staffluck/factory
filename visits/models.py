from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)


class TradePoint(models.Model):
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="tradepoints")


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tradepoint = models.ForeignKey(TradePoint, on_delete=models.CASCADE, related_name="visits")
    latitude = models.FloatField()
    longitude = models.FloatField()
