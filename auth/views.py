from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render


@login_required(login_url='/login')
def dashboard(request):
    return render(request, 'dashboard.html')


def send_email(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        send_mail('Subject goes here', 'Message goes here', 'no-reply@authapplciation.com', [email], fail_silently=False)
        return HttpResponse("Mail Sent to " + email)

    return render(request, 'send_email.html')