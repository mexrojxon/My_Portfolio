from django.contrib import admin
from .models import *

admin.site.register(ResumeModel)
admin.site.register(EducationModel)
admin.site.register(ExperienceModel)
admin.site.register(PortfolioModel)

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['id', 'name']
