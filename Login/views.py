import os
import pickle

import mysql.connector
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages

from Login import trainit
from Login.face_detection import verify
from Login.models import Profile
from operator import itemgetter
import cv2, time

from Login.settings import MEDIA_ROOT


def index(request):
    return render(request, 'sites/StartMenu.html')


def login_user(request):
    return render(request, 'sites/logging.html')


def welcome_user(request):
    if request.method == "POST":
        if Profile.objects.filter(username=request.POST.get('username'),
                                  password=request.POST.get('password')).exists():

            profile = Profile.objects.get(username=request.POST.get('username'), password=request.POST.get('password'))

            name = verify()
            if profile.username == name:
                return render(request, 'sites/Welcome.html', {'profile': profile})
            else:
                context = {'msg' : "unauthorized user access"}
                return render(request, 'sites/logging.html',context)

        else:
            context = {'msg': "Invalid Username or password"}
            return render(request, 'sites/logging.html', context)


def register_user(request):
    # media_path = os.path.join(MEDIA_ROOT, 'profiles\\')
    if request.method == 'POST':
        if request.POST.get('mail') and request.POST.get('username') and request.POST.get('password') \
                and request.FILES.get('photo'):
            saverecord = Profile()
            saverecord.mail = request.POST.get('mail')
            saverecord.username = request.POST.get('username')
            saverecord.password = request.POST.get('password')
            saverecord.photo = request.FILES.get('photo')
            saverecord.save()
            trainit.train()
            messages.success(request, 'New User Registration Details Saved')
            return render(request, 'sites/Registration.html')
    else:
        return render(request, 'sites/Registration.html')
