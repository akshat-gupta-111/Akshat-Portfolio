from django.shortcuts import render
from .forms import Contact
from django.http import HttpResponseRedirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from django.contrib import messages
load_dotenv()

def send_mail(sender_email, receiver_email, app_pass, subject, query, name):
    # Create the email message
    message = MIMEMultipart()
    message["From"] = receiver_email
    message["To"] = receiver_email
    message["Subject"] = subject

    body = subject + " -> " + query + " -via-> "+ sender_email +" ,a.k.a. "+ name
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()  # Secure the connection
        server.login(receiver_email, app_pass)
    
        # Send email
        server.sendmail(receiver_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        server.quit()


def index(request):
    app_pass = os.getenv('APP_PASS')
    receiver_email = os.getenv('RECEIVER_EMAIL')
    if request.method == 'POST':
        form = Contact(request.POST)

        if form.is_valid():
            name = form.cleaned_data['uname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender_email = email
            send_mail(sender_email, receiver_email, app_pass, subject, message, name)
            print(name, email, phone, subject, message)
            messages.success(request, "mail sent!")
            return HttpResponseRedirect('/api/contact/')
    else:
        form = Contact()
    return render(request, "contact/index.html", {'form' : form})