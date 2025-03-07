from django.db import models

class Message(models.Model):
    text = models.TextField()
    is_spam = models.BooleanField(default=False)

    def __str__(self):
        return self.text[:50]
