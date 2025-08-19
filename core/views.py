from django.shortcuts import render
from django.http import HttpResponse

#test comment

def whoami(request):
    # Header arrives as HTTP_X_REMOTE_USER in WSGI environ
    user = request.META.get('HTTP_X_REMOTE_USER', '<unknown>')
    return HttpResponse(f"Logged in as: {user}")
