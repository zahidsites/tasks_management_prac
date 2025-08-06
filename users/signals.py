from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def user_activation_token(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        token_url = f"{settings.BACKEND_URL}/users/activate/{instance.id}/{token}/"
        
        subject = 'Activation token'
        messages = f"Hi {instance.first_name},\n\nPlease activate your acount by clicking the link bellow:\n{token_url}\n\nThank You"
        receipient_list = [instance.email]

        try:
            send_mail(subject,messages,settings.EMAIL_HOST_USER,receipient_list)
        except Exception as e:
            print('Fail to send mail to {instance.email}: {str(e)}')
