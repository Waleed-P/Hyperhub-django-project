from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import ProfileModel

@receiver(post_save,sender=User)
def createporfile(sender,created,instance,**kwargs):
    if created:
        ProfileModel.objects.create(
            user=instance,
            id=instance.id,
            first_name=instance.first_name,
            last_name=instance.last_name,
            email=instance.email
        )