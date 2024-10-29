# track/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import TorqueData  # Import your model here

@receiver(post_save, sender=TorqueData)
def my_handler(sender, instance, created, **kwargs):
    if created:
        print("A new TorqueData instance was created:", instance)
