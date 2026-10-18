#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# check the file to make sure it is working well
def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TrendyFinds.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activatdncsjkncsk/nbse a virtual environment?This is tesing GITHUB conflict"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
