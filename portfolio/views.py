from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import contacts
from .models import gallery
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import uploadform
# Create your views here.


def index(request):
    return render(request, 'index.html')


def gallerys(request):

    image = gallery.objects.all()

    return render(request, 'gallery.html', {'gallerys': image})


def contact(request):
    if request.method == 'POST':
        contact = contacts()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()

    return render(request, 'contact.html')


def imageupload(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = uploadform(request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'imageupload.html', {'form': form})

            imageupload = gallery()
            title = request.POST.get('Title')
            decriptions = request.POST.get('Decriptions')
            drawingImage = request.FILES.get('DrawingImage')

            imageupload.Title = title
            imageupload.Decriptions = decriptions
            imageupload.DrawingImage = drawingImage
            imageupload.save()
        return render(request, 'imageupload.html')

    else:
        # Do something for anonymous users.
        return redirect('loginUser')


def message(request):
    if request.user.is_authenticated:
        message = contacts.objects.all()
        return render(request, 'message.html', {'message': message})
    # Do something for authenticated users.

    else:
        # Do something for anonymous users.
        return redirect('loginUser')


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('imageupload')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('imageupload')
        else:
            messages.info(request, 'invalid user')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('loginUser')
