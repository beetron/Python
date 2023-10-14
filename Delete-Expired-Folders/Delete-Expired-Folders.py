import os
import shutil
import datetime

# Get directory path from environment variable
directory_path = os.getenv("bshare_UploadLocation")

# Set the hours/condition for folder deletion
check_hours = 48
time_now = datetime.datetime.now()

# os.walk to search directory tree
for root, dirs, files in os.walk(directory_path):
    for item in dirs:
        item_path = os.path.join(root, item)
        # Check creation time of folders
        creation_time = datetime.datetime.fromtimestamp(os.path.getctime(item_path))
        # Check how many hours passed since creation
        age = (time_now - creation_time).total_seconds() / 3600  # 3600 for an hour

        if age >= check_hours:
            try:
                shutil.rmtree(item_path)
                print(f"Directory: {item_path} deleted")
            except OSError as e:
                print(f"Error deleting folder: {item_path} - {e}")
