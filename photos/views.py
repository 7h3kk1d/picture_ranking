from django.shortcuts import render, redirect
from django.http import HttpResponse
from photos.models import *
from django.contrib.auth.models import User
import random

def index(request):
    photos = Photo.objects.filter(user=request.user.id)

    random.seed()
    sample = random.sample(photos, 2)

    context = {"photos" : sample}
    return render(request, "photos/index.html", context)

def compare(request):
    if request.method == "POST":
        winner = request.POST["winner"]
        loser = request.POST["loser"]

        try:
            winning_photo = Photo.objects.get(id=winner)
            losing_photo = Photo.objects.get(id=loser)

            winning_photo.rating += 1
            winning_photo.save()
            losing_photo.rating -= 1
            losing_photo.save()
        except Exception as e:
            print e
            print "Photo not found!"

    return redirect('index')

def score(request, poll_id):
    return HttpResponse("The score is %s." % poll_id)
# Create your views here.
