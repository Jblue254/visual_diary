from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    bio = models.TextField(blank=True)

    profile_picture = models.ImageField(
        upload_to='profiles/',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.user.username

class Photo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    image = models.ImageField(
        upload_to="photos/"
    )

    tags = models.CharField(
        max_length=200,
        help_text="Separate tags with commas"
    )

    likes = models.ManyToManyField(
        User,
        related_name="liked_photos",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title