from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from userApp.models import CourseSelection
#from django.contrib.auth. forms import UserCreationForm
from userApp.forms import UserRegistrationForm
def home (request):
    return render(request,'users/home.html')
def register (request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f' Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request,'users/register.html',context)
def course_selection_admin(request):
    selections = CourseSelection.objects.all()
    return render(request, 'users/cs_admin.html', {'selections': selections})
@login_required
def dashboard(request):
    # Logic to display the user dashboard and handle fee details
    return render(request, 'users/dashboard.html')


