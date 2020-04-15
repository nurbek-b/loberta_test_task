from django.db import models


class Url(models.Model):
    url = models.CharField(max_length=255, null=False, help_text="Enter your url")
    check = models.BooleanField(default=True)
    status = models.IntegerField(null=True)

    def __str__(self):
        return self.url



