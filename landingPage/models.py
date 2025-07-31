from django.db import models

class Contact(models.Model):
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Visitor(models.Model):
    ip_address = models.GenericIPAddressField()
    visit_time = models.DateTimeField(auto_now_add=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    referer = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Visitor on {self.visit_time} from IP: {self.ip_address}"