from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, Http404
import datetime
from .models import Students, Scores
from .forms import StudentForm, StudentModelForm

# Create your views here.
@csrf_exempt
def index(request):

    # print('진범', request.method)
    # print('진범', request.GET)
    # print('진범', request.headers)

    # print(request.COOKIES)
    if True:
        request.session['userid'] = 'jinbeom'
    
    
    # request.session['count'] = 0
    # del request.session['userid']


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


def student_modify(request, id):

    # Students.objects.all()
    """
    SELECT *
      FROM students
    """
    # student1 = Students.objects.get(id=id) #데이터 하나, Object
    # student1.name
    # student2 = Students.objects.filter(id=id) #데이터 여러개, 리스트형태
    # student2[0].name
    """
    SELECT *
      FROM students
     WHERE id = 1
    """
    # try:
    #     student = Students.objects.get(pk=id)
    # except:
    #     raise Http404("데이터가 없습니다.")

    student = get_object_or_404(Students, pk=id)

    if request.method == 'GET':
        form = StudentModelForm(instance=student)
        return render(request, 'first/student_modify.html', {
            'form':form
        })
    elif request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect("first:students")
        else:
            return render(request, 'first/student_add.html', {
                'form':form
            })


def student_add(request):
    if request.method == 'GET':
        # form = StudentForm()
        form = StudentModelForm()
        return render(request, 'first/student_add.html', {
            'form':form
        })
    elif request.method == 'POST':
        form = StudentModelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("first:students")
        else:
             return render(request, 'first/student_add.html', {
                'form':form
            })

        # 이건 일반폼
        # form = StudentForm(request.POST)

        # if form.is_valid():
        #     #잘입력됬을경우
        #     Students.objects.create(
        #         name=form.cleaned_data['name'],
        #         address=form.cleaned_data['address'],
        #         email=form.cleaned_data['email']
        #     )
        #     return redirect("first:students")
            
        # else:
        #     return render(request, 'first/student_add.html', {
        #         'form':form
        #     })

        # Students.objects.create(
        #     name=request.POST['name'],
        #     address=request.POST['address'],
        #     email=request.POST['email']
        # )
        

        #return redirect("first:students")
        
        # students = Students.objects.all()
        # return render(request, 'first/students.html', {
        #     'students': students
        # })
    
def score_add(request):

    if request.method == 'GET':
        data = Scores.objects.all()
        return render(request, 'first/score_add.html', {
            'scores': data
        })
    elif request.method == 'POST':
        Scores.objects.create(
            name=request.POST['name'],
            math=request.POST['math'],
            science=request.POST['science'],
            english=request.POST['english']
        )

        return redirect("first:scores")
    

def make_cookie(request, name):
    res = HttpResponse()
    res.set_cookie('name', name)
    return res
