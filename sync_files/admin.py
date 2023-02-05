from django.contrib import admin
from sync_files.models import FileObject, Volume
# Register your models here.
@admin.register(FileObject)
class FileObjectAdmin(admin.ModelAdmin):
    """FileObject admin."""
    
    list_display = ["name", "header_tag", "mime", "checksum"]
    list_filter = ["mime"]

    readonly_fields = ["file_path", "mime", "header_tag", "checksum"]


@admin.register(Volume)
class VolumeAdmin(admin.ModelAdmin):
    """Volume admin"""

    list_display = ["name", "volume_path"]