from django.core.mail import send_mail

from config import settings


def send_email(obj):
    send_mail(
        'Поздравляем',
        f'Ваша запись {obj.name} набрала 100 просмотров. Желаем успехов в дальнейших публикациях',
        settings.EMAIL_HOST_USER,
        ['emikgal2507@gmail.com']
    )
