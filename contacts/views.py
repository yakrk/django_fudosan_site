from django.shortcuts import render, redirect
from .models import Contact
from datetime import datetime
from django.contrib import messages
from django.core.mail import send_mail
import os
import environ
from start.settings import BASE_DIR

# open .env
env = environ.Env(DEBUG=(bool, False))
env.read_env(os.path.join(BASE_DIR, '.env'))

# Create your views here.
def contact(request):
    if request.method == "POST":
        listing_id = request.POST["listing_id"]
        listing = request.POST["listing"]
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST["user_id"]
        realtor_email = request.POST["realtor_email"]

        # check if  had made inquiry already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made your inquiry")
                return redirect('/listings/'+listing_id)
        contact = Contact(
            listing_id=listing_id,
            listing=listing,
            name=name,
            email=email,
            phone=phone,
            message=message,
            user_id=user_id,
            # realtor_email = realtor_email,
        )
        contact.save()

        # send email
        send_mail(
            'Property Listing Inquiry',
            'There has been an inquiry for ' + listing + '. Sign into admin panel for more info',
            env("EMAIL_HOST_USER"),
            [env("EMAIL_HOST_USER")],
            fail_silently=False,
        )

        messages.success(
            request, "Your inquiry has been submitted. A realtor will get back to you soon.")
        return redirect('/listings/'+listing_id)
