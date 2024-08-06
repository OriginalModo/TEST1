from django.db import models


class EmailAccount(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email


class EmailMessage(models.Model):
    subject = models.CharField(max_length=255)
    sent_at = models.DateTimeField()
    received_at = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    attachments = models.FileField(upload_to='attachments/', blank=True, null=True)

    def __str__(self):
        return self.subject