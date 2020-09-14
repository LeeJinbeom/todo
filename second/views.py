from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponseForbidden
from .models import Favourite, Todo, User
from .forms import FavouriteModelForm, TodoModelForm, SignupForm, LoginForm

# Create your views here.
def index(request):
    print(request.user.is_authenticated)
    print(request.user)
    return render(request, "second/index.html")

@login_required
def favourite(request):
    data = Favourite.objects.filter(reg_user=request.user)
    return render(request, "second/favourite.html",
        {'datas':data}
    )

@login_required
def favourite_detail(request, seq):
    try:
        detail = Favourite.objects.get(pk=seq, reg_user=request.user)
    except:
        return HttpResponseForbidden()
    
    #detail = get_object_or_404(Favourite, pk=seq, reg_user=request.user)

    #detail = Favourite.objects.get(seq=seq)
    return render(request, "second/favourite_detail.html",{
        'detail': detail
    })

@login_required
def favourite_add(request):
    if request.method == 'GET':
        form = FavouriteModelForm()
        return render(request, "second/favourite_add.html", {
            'form': form
        })
    elif request.method == 'POST':

        reg_user = Favourite(reg_user=request.user)
        form = FavouriteModelForm(request.POST, instance=reg_user)

        if form.is_valid():
            favourite = form.save()
            return redirect("second:favourite_detail", favourite.seq)
        else:
            return render(request, "second/favourite_add.html", {
                'form': form
            })

@login_required
def favourite_modify(request, seq):

    try:
        detail = Favourite.objects.get(pk=seq, reg_user=request.user)
    except:
        return HttpResponseForbidden()

    if request.method == 'GET':
        form = FavouriteModelForm(instance=favourite)
        return render(request, "second/favourite_modify.html", {
            'form': form
        })
    elif request.method == 'POST':
        form = FavouriteModelForm(request.POST, instance=favourite)
        if form.is_valid():
            favourite = form.save()
            return redirect("second:favourite_detail", favourite.seq)
        else:
            return render(request, "second/favourite_modify.html", {
                'form': form
            })

@login_required
def favourite_delete(request, seq):
    
    try:
        detail = Favourite.objects.get(pk=seq, reg_user=request.user)
    except:
        return HttpResponseForbidden()

    favourite.delete()
    return redirect("second:favourite")

@login_required
def todo(request):
    
    pendings = Todo.objects.filter(status='pending', reg_user=request.user)
    inprogresss = Todo.objects.filter(status='inporgress', reg_user=request.user)
    ends = Todo.objects.filter(status='end', reg_user=request.user)
    
    # data = Todo.objects
    
    # if 'group' in request.GET:
    #     data = data.filter(group__name=request.GET['group'])
    
    # if 'end_date' in request.GET:
    #     data = data.filter(end_date__gte=request.GET['end_date'])
    
    return render(request, "second/todo.html",
        {
            'pendings':pendings,
            'inprogresss':inprogresss,
            'ends':ends
        }
    )

@login_required
def todo_detail(request, seq):

    try:
        detail = Todo.objects.get(pk=seq, reg_user=request.user)
    except:
        return HttpResponseForbidden()

    return render(request, "second/todo_detail.html", {
        'detail': detail
    })

@login_required
def todo_add(request):
    if request.method == 'GET':
        form = TodoModelForm()
        return render(request, "second/todo_add.html", {
            'form': form
        })
    elif request.method == 'POST':

        todo = Todo(reg_user=request.user)
        form = TodoModelForm(request.POST, instance=todo)

        if form.is_valid():
            todo = form.save()
            return redirect("second:todo_detail", todo.seq)
        else:
            return render(request, "second/todo_add.html", {
                'form': form
            })

@login_required
def todo_modify(request, seq):

    try:
        todo = Todo.objects.get(pk=seq, reg_user=request.user)
    except:
        return HttpResponseForbidden()
   

    if request.method == 'GET':
        form = TodoModelForm(instance=todo)
        return render(request, "second/todo_modify.html", {
            'form': form
        })
    elif request.method == 'POST':
        form = TodoModelForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save()
            return redirect("second:todo_detail", todo.seq)
        else:
            return render(request, "second/todo_modify.html", {
                'form': form
            })

@login_required
def todo_delete(request, seq):

    try:
        todo = Todo.objects.get(pk=seq, reg_user=request.user)
    except:
        return HttpResponseForbidden()

    todo.delete()
    return redirect("second:todo")

def signup(request):

    if request.method == 'GET':
        form = SignupForm()
        return render(request, "second/signup.html", {
            'form': form
        })
    elif request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("second:index")
        else:
            return render(request, "second/signup.html", {
                'form': form
            })

def signin(request):

    if request.method == 'GET':
        form = LoginForm()
        return render(request, "second/login.html", {
            'form': form
        })
    elif request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("second:index")
        else:
            return render(request, "second/login.html", {
                'form': form
             })

def logout_view(request):
    logout(request)
    return redirect("second:index")
