
from celery import shared_task
import celery
# from celery.app import task
from django.core.mail import send_mail
from .models import *


@shared_task
def order_created(order_id):
    """
    Task to send an email-notification when an order is successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = f"Order nr. {order.id}"
    message = f"Dear {order.first_name}, \n\n" \
              f"you have successfully placed an order." \
              f"Your order ID is {order.id}."
    mail_sent = send_mail(
        subject, message, 'admin@myshop.com', [order.email]
    )
