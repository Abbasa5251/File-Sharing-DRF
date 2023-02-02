from rest_framework import serializers
from .models import Folder, File
from .utils import zip_files

class FileListSerializer(serializers.Serializer):
    files = serializers.ListField(child=serializers.FileField(max_length=124000, allow_empty_file=False, use_url=False))
    folder = serializers.CharField(max_length=256, read_only=True)

    def create(self, validated_data):
        folder = Folder.objects.create()
        files = validated_data.pop('files')
        file_objs = list()
        for file in files:
            file_obj = File.objects.create(folder=folder, file=file)
            file_objs.append(file_obj)
        zip_files(folder.uid)
        
        return {
            'files': files,
            'folder': str(folder.uid),
        }