from django.shortcuts import render, redirect
from ast import Param
from django.contrib import messages
#from contextlib import _RedirectStream
from django.shortcuts import render
from django.contrib.auth.models import User, auth
# Create your views here.
from datetime import date, datetime

#from time import time
from django.shortcuts import render
#from django.db.models import Q
from navigate.models import HeaderAddvertise, BrowserIcon, Logo, StockReport, Titles, Tricker, FooterHeadlinea, FooterHeadlineb, FooterHeadlinec, FooterHeadlined, FooterHeadlinee, FooterHeadlinef, LeaveCommentArea, FooterBgImg, FooterWidgetLista,FooterWidgetListb, FooterWidgetListc, FooterWidgetListd, FooterWidgetListe, FooterWidgetListf
from navigate.models import NavItem, NavItemDropDown
from navigate.models import BreakingNewsTitle
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUsers, CommentPerson
#from accounts.models import Registration
# Create your views here.

def subscribe(request):
    if request.method=='POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)
        if not name or not email:
            messages.error(request, "You must Give the name and email to subscribe our newsletter")
            return redirect("/")

        if User.objects.filter(email=email).first():
            messages.error(request, f"Found Registered user with associated {email} email, you must login to subscribe or unsubscribe!")
            return redirect(request.META.get("HTTP_REFFERER", "/"))

        subscribed_users = SubscribedUsers.objects.filter(email=email).first()
        if subscribed_users:
            messages.error(request, f"{email} email is already a subscriber!")
            return redirect(request.META.get("HTTP_REFFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribed_model_instance = SubscribedUsers()
        subscribed_model_instance.name = name
        subscribed_model_instance.email = email
        subscribed_model_instance.save()
        messages.success(request, f"{email} Email was successfully subscribed to our newslettter!")
        return redirect(request.META.get("HTTP_REFFERER", "/"))


def comment(request):
    if request.method == 'POST':
        txt = request.POST.get('txt')
        email = request.POST.get('email')
        mssg = request.POST.get('mssg')
        if not txt or not email or not mssg:
            messages.error(request, "You must Give the Name, email and your message")
        commentperson = CommentPerson.objects.create(txt = txt, email = email, mssg = mssg)
        commentperson.save()
        messages.success(request, 'You are commented successfully!')
        return redirect("/")
        










