import subprocess


def comando(self):
    subprocess.run(["python manage.py store_launching_data"])