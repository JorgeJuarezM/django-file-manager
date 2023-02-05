from django.db import models
import uuid
# Create your models here.
class FileObject(models.Model):
    # Identification
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Data
    checksum = models.CharField(max_length=32, blank=False, null=True)
    file_path = models.CharField(max_length=255, unique=True, blank=False, null=False)
    header_tag = models.CharField(max_length=255)
    mime = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=False, null=True)

class Volume(models.Model):
    # Identification
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Data
    name = models.CharField(max_length=255, blank=False, null=False)
    volume_path = models.CharField(max_length=255, unique=True, blank=False, null=False)