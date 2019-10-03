from django.core.paginator import Paginator
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.conf import settings

def paginator_class(users_list, page_no, records_per_page=10):
    paginator = Paginator(users_list, records_per_page)
    try:
        users = paginator.page(page_no)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return users