from django.http import HttpResponse
from django.template import loader

from .models import Choice, Question


def index(request):
    template = loader.get_template("event/index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}.")


def create(request):
    #
    return HttpResponse("")
