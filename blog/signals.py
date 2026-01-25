from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os
from blog.models import PostImage

@receiver(pre_delete, sender=PostImage)
def delete_image_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)