from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from . import service

def index(request):
    return render(request, "index.html")

def redirect_hash(request, url_hash):
    original_url = service.load_url(url_hash).original_url
    return redirect(original_url)

def simplify_url(request) -> HttpResponse:
    if request.method == "POST":
        url = request.POST.get("url")

        if "http" not in url:
            url = f"https://{url}"

        validator = service.validate_url(url)
        if not validator:
            return HttpResponse("Looks like you entered an incorrect or empty URL")

        response = service.check_url_for_existance(url)
        if not response:
            return HttpResponse("Looks like you entered a non-existent URL")

        simplified_url_hash = service.simplify(url)
        simplified_url = request.build_absolute_uri(reverse("redirect", args=[simplified_url_hash]))

        return HttpResponse(simplified_url)

    return HttpResponse("Something went wrong!")
