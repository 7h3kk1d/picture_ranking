from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")
def score(request, poll_id):
    return HttpResponse("The score is %s." % poll_id)
# Create your views here.
