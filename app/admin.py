from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(Result)
class GeneralUserAdmin(UserAdmin):
	model = GeneralUser

	fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('full_name','phone',"usertype")}),
    )


admin.site.register(GeneralUser,GeneralUserAdmin)
