from django.db import models
from django.db import models
from account.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    first_name = models.CharField(max_length=128, blank=True, null=True)
    last_name = models.CharField(max_length=128, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatar/', blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    github_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.user.email

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    
    if created:
        Profile.objects.create(user=instance)