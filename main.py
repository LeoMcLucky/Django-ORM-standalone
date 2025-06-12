import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Общее количество пропусков:', Passcard.objects.count())  # noqa: T001
    print('Количество активных пропусков:', len(
        Passcard.objects.filter(is_active=True)))
