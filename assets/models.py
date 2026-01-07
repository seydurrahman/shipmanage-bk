from django.db import models

class Asset(models.Model):
    item = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.total_amount = self.quantity * self.rate
        super().save(*args, **kwargs)

    def __str__(self):
        return self.item
