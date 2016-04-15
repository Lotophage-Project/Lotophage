import os
import sys

from django.utils.crypto import get_random_string


def setup_django_secret_key():
    """
    Helper for setting up a secret key for developing so the Django
    settings file avoid a hard coded value.

    This function checks if a file ``.django_secret_key.txt`` exists and
    uses the file content as value for the environment variable
    DJANGO_SECRET_KEY. The file is created if it does not exist.
    """
    secret_key_file = os.path.join(
        os.path.dirname(__file__), '.django_secret_key.txt')
    if not os.path.exists(secret_key_file):
        secret_key = get_random_string(
            50,
            'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)')
        with open(secret_key_file, 'w') as f:
            f.write(secret_key)
    else:
        with open(secret_key_file) as f:
            secret_key = f.read().strip()
    os.environ['DJANGO_SECRET_KEY'] = secret_key


if __name__ == '__main__':
    setup_django_secret_key()

    os.environ.setdefault(
        'DJANGO_SETTINGS_MODULE',
        'lotophage.lotophage_server.settings')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
