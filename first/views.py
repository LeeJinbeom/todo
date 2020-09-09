from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from .models import Students, Scores

# Create your views here.
@csrf_exempt
def index(request):

    print('진범', request.method)
    print('진범', request.GET)
    print('진범', request.headers)

    return render(request, 'first/index.html')


def students_detail(request, id):

    print("한번찍어보기", id)
    students = Students.objects.get(pk=id)

    return render(request, 'first/students_detail.html', {
        'student': students
    })


def students(request):
    """
    print('진범', request.method)
    print('진범', request.GET)
    print('진범', request.headers)
    """
    
    students = Students.objects.all()

    return render(request, 'first/students.html', {
        'text': 'Hello World! Hello World! Hello World!',
        'date': datetime.datetime.now,
        'students': students
    })

def scores(request):
    scores = Scores.objects.all()

    #render(request, 템플릿경로 TEXT, 보낼데이터 DICT
    return render(request, 'first/score.html', {
        'scores':scores
    })
