from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.hashers import make_password
from django.conf import settings

from concert.forms import LoginForm, SignUpForm
from concert.models import Concert, ConcertAttending
import requests


# Create your views here.

def signup(request):
    pass


def index(request):
    return render(request, "index.html")


def songs(request):
    songs = requests.get(settings.SONGS_API_URL).json()["songs"]
    return render(request, "songs.html", {"songs": songs})


def photos(request):
    photos = requests.get(settings.PHOTOS_API_URL).json()
    return render(request, "photos.html", {"photos": photos})

def login_view(request):
    pass

def logout_view(request):
    pass

def concerts(request):
    pass


def concert_detail(request, id):
    if request.user.is_authenticated:
        obj = Concert.objects.get(pk=id)
        try:
            status = obj.attendee.filter(user=request.user).first().attending
        except:
            status = "-"
        return render(request, "concert_detail.html", {"concert_details": obj, "status": status, "attending_choices": ConcertAttending.AttendingChoices.choices})
    else:
        return HttpResponseRedirect(reverse("login"))
    pass


def concert_attendee(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            concert_id = request.POST.get("concert_id")
            attendee_status = request.POST.get("attendee_choice")
            concert_attendee_object = ConcertAttending.objects.filter(
                concert_id=concert_id, user=request.user).first()
            if concert_attendee_object:
                concert_attendee_object.attending = attendee_status
                concert_attendee_object.save()
            else:
                ConcertAttending.objects.create(concert_id=concert_id,
                                                user=request.user,
                                                attending=attendee_status)

        return HttpResponseRedirect(reverse("concerts"))
    else:
        return HttpResponseRedirect(reverse("index"))


def signup(request):
    return HttpResponseRedirect("/admin/")


def login_view(request):
    return HttpResponseRedirect("/admin/login/?next=/concerts/")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def concerts(request):
    if request.user.is_authenticated:
        lst = []
        for item in Concert.objects.all():
            try:
                status = item.attendee.filter(user=request.user).first().attending
            except Exception:
                status = "-"
            lst.append({"concert": item, "status": status})
        return render(request, "concerts.html", {"concerts": lst})
    return HttpResponseRedirect(reverse("login"))
