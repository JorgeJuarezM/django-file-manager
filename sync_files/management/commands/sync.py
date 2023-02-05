from django.core.management.base import BaseCommand, CommandError
from typing import Any, Optional
import os
import magic
from sync_files.models import FileObject, Volume
import hashlib

class Command(BaseCommand):
    """Command"""

    def sync_folder(self, folder_path):
        files = os.listdir(folder_path)
        for file in files:
            file_path = os.path.join(folder_path, file)
            if os.path.islink(file_path):
                continue

            if os.path.isdir(file_path):
                self.sync_folder(file_path)
                continue

            file_hash = hashlib.md5()
            with open(file_path, "rb") as f:
                while chunk := f.read(8192):
                    file_hash.update(chunk)

            checksum = file_hash.hexdigest()
            file_qs = FileObject.objects.filter(checksum=checksum)
            if file_qs.exists():
                continue

            mime = magic.from_file(file_path, mime=True)
            header = magic.from_file(file_path)

            file_obj = FileObject(
                checksum=checksum,
                file_path=file_path,
                header_tag=header,
                mime=mime,
                name=file,
            )

            file_obj.save()

    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        """Handle"""
        volumes = Volume.objects.all()
        for volume in volumes.iterator():
            self.sync_folder(volume.volume_path)