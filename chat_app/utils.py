from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_invitation_email(inviter, invitee, chat_room):
    subject = 'You have been invited to a chat room'
    from_email = settings.EMAIL_FROM
    recipient_list = [invitee.email]

    context = {'inviter': inviter, 'invitee': invitee, 'chat_room': chat_room}
    html_message = render_to_string('chat/email/invitation.html', context)
    plain_message = render_to_string('chat/email/invitation.txt', context)

    send_mail(
        subject,
        plain_message,
        from_email,
        recipient_list,
        html_message=html_message,
        fail_silently=False,
    )
