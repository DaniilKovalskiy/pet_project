from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    image = models.ImageField(upload_to='users_images', null=True, blank=True,
                              default="vendor/img/users/default_avatar.jpg")
