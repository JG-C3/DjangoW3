#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'intro.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "장고 오류 "
            "del c: 를 실행하고 다시 시도해주세요 "
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
