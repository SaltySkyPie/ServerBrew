from django.db import models
import uuid
from django.utils import timezone


class Order(models.Model):
    STATUS_CHOICES = [
        ('ordered', 'Ordered'),
        ('ready', 'Ready for Collection'),
        ('collected', 'Collected'),
    ]
    DRINK_CHOICES = [
        ('Caffe Latte', 'Caffe Latte'),
        ('Cappuccino', 'Cappuccino'),
        ('Espresso', 'Espresso'),
        ('Mocha', 'Mocha'),
        ('Macchiato', 'Macchiato'),
        ('Flat White', 'Flat White'),
        ('Affogato', 'Affogato'),
        ('Americano', 'Americano'),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    order_number = models.PositiveIntegerField(
        choices=[(i,str(i)) for i in range(1, 100)])
    drink = models.CharField(max_length=100, choices=DRINK_CHOICES)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default='ordered')
    created_at = models.DateTimeField(default=timezone.now)
    total_preparing_time = models.IntegerField(null=True)

    @property
    def waiting_time(self):
        if not self.total_preparing_time:
            return f"{(timezone.now() - self.created_at).seconds // 60}:{(timezone.now() - self.created_at).seconds % 60:02}"
        return f"{self.total_preparing_time // 60}:{self.total_preparing_time % 60:02}"


    def __str__(self):
        return f"Order #{self.order_number}: {self.drink} - {self.get_status_display()}"
