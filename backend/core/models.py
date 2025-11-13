from django.db import models

class CompanyInfo(models.Model):
    name = models.CharField(max_length=255, help_text="Company's official name")
    logo = models.ImageField(upload_to='logos/', null=True, blank=True, help_text="Company's logo")
    address = models.TextField(help_text="Company's physical address")
    phone_number = models.CharField(max_length=20, help_text="Contact phone number")
    email = models.EmailField(help_text="Contact email address")
    website = models.URLField(help_text="Company's website")
    currency = models.CharField(max_length=10, help_text="Default currency (e.g., USD, SAR)")
    timezone = models.CharField(max_length=50, default='UTC', help_text="Default timezone (e.g., Asia/Riyadh)")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"
