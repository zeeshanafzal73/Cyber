from django.shortcuts import render

from .models import Questions


# Create your views here.

def index(request):
    random_questions = Questions.objects.order_by('?')[:4]
    context = {
        'random_questions': random_questions
    }
    return render(request, 'index.html', context)
