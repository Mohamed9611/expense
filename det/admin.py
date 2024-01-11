from django.contrib import admin
from .models import Expense, Profile

# Register your models here.

class ExpenseAdmin(admin.ModelAdmin):
  list_display = ("user", "date", "category","amount")


admin.site.register(Expense,ExpenseAdmin)

class ProfileAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "phone",)


admin.site.register(Profile,ProfileAdmin)