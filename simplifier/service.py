import random
import string
import requests

from django.utils import timezone
from django.forms import ValidationError
from django.core.validators import URLValidator


from .models import Simplifier

def simplify(url):
    random_hash = "".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(7))
    mapping = Simplifier(original_url=url, hash=random_hash, creation_date= timezone.now())
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

def check_url_for_existance(url):
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