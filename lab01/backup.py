import os
import shutil
import zipfile

home = "/home/student"
backup = "/home/student/backup"

for e in os.listdir(home):
    if os.path.isfile(os.path.join(home, e)):
        shutil.copy(os.path.join(home, e), backup)

with zipfile.ZipFile("backup.zip", "w") as new_zip:
    for e in os.listdir(backup):
        if os.path.isfile(os.path.join(backup, e)):
            new_zip.write(os.path.join(backup, e))

