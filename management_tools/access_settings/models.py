from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class AccessSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user")
    def __str__(self):
        return self.user.username

class Setting(models.Model):
    access_setting = models.ForeignKey(AccessSetting, on_delete=models.CASCADE, related_name="access_setting")
    name = models.CharField(verbose_name = "name", max_length = 32)
    setting = models.JSONField(verbose_name="setting")
    def __str__(self):
        return self.name

@receiver(post_save, sender=User)
def create_user_wallet(sender, instance, created, **kwargs):
    if created:
        AccessSetting.objects.create(user = instance)