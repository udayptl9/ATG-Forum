from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import AutherRegisterForm
import random
from django.contrib import messages
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = AutherRegisterForm(request.POST)
        if form.is_valid():
            num1 = request.session.get('num1')
            operator = request.session.get('operator')
            num2 = request.session.get('num2')
            user_answer = request.POST['captcha']
            if operator == '+':
                answer = num1 + num2
            elif operator == '-':
                answer = num1 - num2
            if int(user_answer) == int(answer):
                form.save()
                request.session['num1'] = ''
                request.session['operator'] = ''
                request.session['num2'] = ''
                messages.success(request, 'Auther successfully Added, Please Login')
                return redirect('login')
            else:
                messages.error(request, 'Enter the correct answer')
                return redirect('register')
    else:
        form = AutherRegisterForm()
        num1 = random.randint(50, 100)
        num2 = random.randint(0, 50)
        operator_choices = ['+', '-', ]
        operator = random.choice(operator_choices)
        request.session['num1'] = num1
        request.session['operator'] = operator
        request.session['num2'] = num2
        context = {'form': form, 'num1': num1,
                   'num2': num2, 'operator': operator}
    return render(request, 'authers/register.html', context)


def home(request):
    return redirect('home')
