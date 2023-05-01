from celery import shared_task
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import Certificate
from InfoOt.celery import app
from .service import send

# @shared_task
# def mailing_monday():
#     qs = Certificate.objects.filter(time=0)
#     msg = EmailMultiAlternatives(
#         subject=f"Закончилось удостоверение'",
#         body=qs,
#         from_email='vachrameev.oleg@yandex.ru',
#         to=['zigulatnatria@yandex.ru'],
#     )
#     msg.send()
#


@shared_task
def certificate_created(certificate_id):
 """
 Задание по отправке уведомления по электронной почте
 при успешном создании заказа.
 """
 certificate = Certificate.objects.get(id=certificate_id)
 subject = f'Order nr. {certificate.id}'
 message = f'Dear {certificate.name_certificate},\n\n' \
 f'You have successfully placed an order.' \
 f'Your order ID is {certificate.id}.'
 mail_sent = send_mail(subject, message,
                       'vachrameev.oleg@yandex.ru',
                       ['zigulatnatria@yandex.ru']
                       )
 return mail_sent

@app.task
def send_test_email(user_email):
    send(user_email)