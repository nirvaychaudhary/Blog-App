from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EntryModel(models.Model):
    entry_image = models.ImageField(null=True, blank=True, upload_to="images/")
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.entry_title