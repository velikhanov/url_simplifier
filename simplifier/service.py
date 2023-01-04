import random
import string
import requests

from django.utils import timezone
from django.forms import ValidationError
from django.core.validators import URLValidator


from .models import Simplifier

def simplify(url, ip):
    is_already_exists = Simplifier.objects.filter(original_url=url, ip=ip).exists()
    if is_already_exists:
        return Simplifier.objects.get(original_url=url, ip=ip).hash

    random_hash = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = Simplifier(original_url=url, hash=random_hash, ip=ip, creation_date= timezone.now())
    mapping.save()
    return random_hash

def load_url(url_hash):
    return Simplifier.objects.get(hash=url_hash)
    

def validate_url(url: str) -> bool:
    validator = URLValidator()
    try:
        validator(url)
        return True
    except ValidationError:
        return False

def check_url_for_existance(url: str) -> bool:
    try:
        requests.get(url).ok
        return True
    except requests.HTTPError:
        return False
    except requests.exceptions.Timeout:
        return False
    except requests.exceptions.TooManyRedirects:
        return False
    except requests.exceptions.RequestException:
        return False

def get_client_ip(request) -> str:
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip