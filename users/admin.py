from django.contrib import admin
from .models import User
# Register your models here.

class EMSAdmin(admin.ModelAdmin):
    list_display = ('email','name')
    list_filter = ('email',)


admin.site.site_header = "WebllistoEMS"
# admin.site.register(User)
admin.site.register(User,EMSAdmin)

