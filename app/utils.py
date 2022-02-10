import os
import shutil

def get_upload_path(instance, filename):
    return os.path.join(str(instance.folder.uid), filename)

def zip_files(folder):
    shutil.make_archive(f"public/static/zip/{folder}", 'zip', f"public/static/{folder}")
