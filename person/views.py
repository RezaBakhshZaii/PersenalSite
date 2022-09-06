from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import *


def get_info():
    skill = Skills.objects.all().order_by("-progress")
    project = Project.objects.all()
    information = Information.objects.all()
    data = {
        'skill': skill,
        'project': project,
        'information': information
    }
    return data
# Create your views here.
def index(requests):
    template = loader.get_template('page.html')
    return HttpResponse(template.render(get_info(), requests))


def messages(requests):
    name = requests.POST.get('name')
    email = requests.POST.get('email')
    descrip = requests.POST.get('descrip')
    message = requests.POST.get('message')

    name_length = len(name)
    email_length = len(email)
    descrip_length = len(descrip)
    message_length = len(message)
    if name_length == 0 or email_length == 0 or descrip_length == 0 or message_length == 0:
        data = get_info()
        data["name"] = name_length
        data["email"] = email_length
        data["descrip"] = descrip_length
        data["message"] = message_length
        template = loader.get_template('page.html')
        return HttpResponse(template.render(data, requests))
    comment = Messages(name=name, email=email, description=descrip, message=message)
    comment.save()
    return HttpResponseRedirect(reverse('index'))

