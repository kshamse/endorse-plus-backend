from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Profile(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250, null=True, blank=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    linkedin_profile_url = models.URLField(max_length=300, blank=True)
    summary = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/',
        default='../default_profile_llqwrh'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name}"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance, name=instance.username)


post_save.connect(create_profile, sender=User)
