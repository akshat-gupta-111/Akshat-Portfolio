from django.shortcuts import render
from .forms import Contact
from django.http import HttpResponseRedirect
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from django.contrib import messages
from django.conf import settings
load_dotenv()


def send_mail_via_mailtrap(sender_email, subject, query, name):
    """Send email using Mailtrap SMTP"""
    receiver_email = os.getenv('RECEIVER_EMAIL')
    
    # Create the email message
    message = MIMEMultipart()
    message["From"] = settings.EMAIL_HOST_USER  # Mailtrap sandbox sender
    message["To"] = receiver_email  # Your email from .env
    message["Subject"] = subject

    body = f"{subject} -> {query} -via-> {sender_email} ,a.k.a. {name}"
    message.attach(MIMEText(body, "plain"))

    try:
        # Connect to Mailtrap's SMTP server
        server = smtplib.SMTP(settings.EMAIL_HOST, int(settings.EMAIL_PORT))
        server.starttls()  # Secure the connection
        server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    
        # Send email
        server.sendmail(settings.EMAIL_HOST_USER, receiver_email, message.as_string())
        print("Email sent successfully via Mailtrap!")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
    finally:
        server.quit()


def index(request):
    if request.method == 'POST':
        form = Contact(request.POST)

        if form.is_valid():
            name = form.cleaned_data['uname']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message_text = form.cleaned_data['message']
            
            if send_mail_via_mailtrap(email, subject, message_text, name):
                print(name, email, phone, subject, message_text)
                messages.success(request, "Mail sent successfully!")
            else:
                messages.error(request, "Failed to send mail. Please try again.")
            return HttpResponseRedirect('/api/contact/')
    else:
        form = Contact()
    return render(request, "contact/index.html", {'form' : form})