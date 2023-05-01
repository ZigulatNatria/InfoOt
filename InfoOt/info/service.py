from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'тестовое сообщение',
        'текст тестового сообщения',
        'vachrameev.oleg@yandex.ru',
        [user_email],
        fail_silently=False,
    )