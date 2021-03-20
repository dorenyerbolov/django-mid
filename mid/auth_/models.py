from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    ADMIN = 1
    GUEST = 2
    USER_ROLE_CHOICES = (
        (ADMIN, 'Admin'),
        (GUEST, 'Guest')
    )

    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, verbose_name='Биография')
    location = models.CharField(max_length=30, blank=True, verbose_name='Локация')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
    role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES, default=GUEST)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return f"{self.user}"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
