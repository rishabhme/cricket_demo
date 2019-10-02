from django.core.paginator import Paginator
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.conf import settings

def generate_random_string(length):
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    random_string = get_random_string(length, chars)

    return random_string


def send_password_email(email, password):
    subject = 'User Password'
    from_email = settings.DEFAULT_FROM_EMAIL
    to_email = [email]
    message = " Enter {1} with {0} Password to Login".format(
        password,email)

    send_mail(
        subject,
        message,
        from_email,
        to_email,
        fail_silently=True,
    )

    return None


def paginator_class(users_list, page_no, records_per_page=10):
    paginator = Paginator(users_list, records_per_page)
    try:
        users = paginator.page(page_no)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return users