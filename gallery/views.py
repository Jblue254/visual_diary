from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm
from .models import Photo


def home(request):
    tag = request.GET.get("tag")

    photos = Photo.objects.all().order_by("-created_at")

    if tag:
        photos = photos.filter(tags__icontains=tag)

    return render(
        request,
        "gallery/home.html",
        {"photos": photos}
    )

def photo_detail(request, pk):
    photo = get_object_or_404(
        Photo,
        pk=pk
    )

    return render(
        request,
        "gallery/photo_detail.html",
        {"photo": photo}
    )


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )


@login_required
def profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()

    else:
        form = ProfileForm(instance=profile)

    return render(
        request,
        "gallery/profile.html",
        {
            "form": form,
            "profile": profile
        }
    )