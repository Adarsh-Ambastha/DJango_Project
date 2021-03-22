from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.contrib.auth.models import User
# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        customer_need =request.POST['customer_need']

        if request.user.is_authenticated:

            has_contacted = Contact.objects.all().filter(car_id = car_id , user_id = user_id)
            if has_contacted:
                messages.error(request, 'You have already inquired about this car we will get back to you shortly')
                return redirect('/cars/'+car_id)

        contact = Contact(car_id = car_id, car_title = car_title, user_id = user_id, first_name = first_name, last_name = last_name,
                            customer_need = customer_need, city = city, state = state, email = email, phone = phone, message = message)

        admin_info = User.objects.get(is_superuser =True)
        admin_email = admin_info.email
        send_mail (
                    'New Car inquiry on your website',
                    'you have a new inquiry for the car '+car_title + '.Login to your admin pannel for more details',
                    'adarshambastha18@gamil.com',
                    [admin_email],
                    fail_silently=False,
                )

        contact.save()
        messages.success(request,"your request has been submitted , we will get ack to you shortly")
        return redirect('/cars/'+car_id)
