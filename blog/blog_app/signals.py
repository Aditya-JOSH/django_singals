from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
import time
import threading


@receiver(post_save, sender=Post)
def post_created(sender, instance, **kwargs):
    print("Signal received, starting sleep...")
    time.sleep(5)  # I have added a delay to show synchronous execution
    print("Signal processing finished.")

@receiver(post_save, sender=Comment)
def comment_created(sender, instance, **kwargs):
    print(f"Signal is running in thread: {threading.current_thread().name}")

@receiver(post_save, sender=User)
def user_created(sender, instance, **kwargs):
    print("Signal received, raising exception to test transaction rollback.")
    raise ValueError("Testing transaction rollback with signal.")