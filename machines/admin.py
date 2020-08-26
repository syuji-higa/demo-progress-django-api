from django.contrib import admin
from .models import Machine
from adminsortable.admin import SortableAdmin

class MachineAdmin(SortableAdmin):
    list_display = ("id", "name", "progress")
    list_display_links = ("id", "name", "progress")

admin.site.register(Machine, MachineAdmin)
