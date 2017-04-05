from django.db import models
from cms.models import CMSPlugin


class ContactUSModel(CMSPlugin):
    """
    Contact Us Model
    """
    first_name = models.CharField(max_length=150, verbose_name="Full Name")
    last_name = models.CharField(max_length=150, verbose_name="Full Name")
    email_address = models.EmailField(max_length=200, verbose_name="Email Address")
    contact_number = models.IntegerField(max_length=10, verbose_name="Contact Number")
    comment_box = models.TextField(max_length=2000, verbose_name="Text Area")

    def __str__(self):
        return self.first_name
