from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"Employee: {self.name}"

class TradePoint(models.Model):
    title = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="tradepoints")

    def __str__(self):
        return f"TradePoint: {self.title}"

class Visit(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    tradepoint = models.ForeignKey(TradePoint, on_delete=models.CASCADE, related_name="visits")
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return f"Visit In {self.tradepoint.title} by {self.tradepoint.employee.name} on {self.created_at}"
