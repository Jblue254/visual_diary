from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, ProfileForm, PhotoForm
from .models import Profile, Photo


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
    profile, created = Profile.objects.get_or_create(
        user=request.user
    )

    if request.method == "POST":
        form = ProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect("profile")

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


@login_required
def like_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    photo.likes.add(request.user)
    photo.dislikes.remove(request.user)

    return redirect("photo_detail", pk=pk)


@login_required
def dislike_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)

    photo.dislikes.add(request.user)
    photo.likes.remove(request.user)

    return redirect("photo_detail", pk=pk)
@login_required
def upload_photo(request):

    if request.method == "POST":

        form = PhotoForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = PhotoForm()

    return render(
        request,
        "gallery/upload_photo.html",
        {"form": form}
    )