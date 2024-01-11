from django.db import models
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import User

'''
# Create your models here.
class MultiFormatDateField(models.DateField):
    def to_python(self, value):
        if isinstance(value, datetime):
            return value
        if value:
            for fmt in ['%d/%m/%Y', '%d-%m-%Y', '%Y-%m-%d']:
                try:
                    return datetime.strptime(value, fmt).date()
                except ValueError:
                    pass
            raise ValidationError('Invalid date format. Please use dd/mm/yyyy, dd-mm-yyyy, or yyyy-mm-dd.')

    def get_prep_value(self, value):
        return value.strftime('%Y-%m-%d')
'''

class Expense(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)


    category_choices = [
        ('food','Food'),
        ('utilities','Utilities'),
        ('transportation','Transportation'),
        ('entertainment','Entertainment'),
        ('clothing','Clothing'),
        ('healthcare','Healthcare'),
        ('education','Education'),
        ('housing','Housing'),
        ('technology','Technology'),
        ('travel','Travel'),
        ('gifts','Gifts'),
        ('subscription','Subscription'),
        ('miscellaneous','Miscellaneous'),
    ]

    expense_title = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now())
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=category_choices)

    

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('delete', 'Delete'),
        ('trash', 'Trash'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    def __str__(self):
        return f"{self.user} - {self.date} - {self.category} - {self.amount}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile - {self.first_name} - {self.last_name}"