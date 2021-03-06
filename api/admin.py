from django.contrib import admin
from .forms import DataFileForm

# Register your models here.
from .models import DataFile, SmartHomeDevice

class DataFileAdmin(admin.ModelAdmin):
    form = DataFileForm
    # override the save method to include the data_file_hash
    def save_model(self, request, obj, form, change):
        obj.data_file_hash = form.cleaned_data['data_file_hash']
        obj.save()

admin.site.register(DataFile, DataFileAdmin)
admin.site.register(SmartHomeDevice)
