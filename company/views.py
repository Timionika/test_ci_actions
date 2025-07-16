from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    user = request.user
    return render(request, "index.html", {"user": user})


@login_required
def profile(request):
    user = request.user
    return render(request, "profile.html", {"user": user})
