from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from .utils import DataMixin
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # создание объекта без сохранения в БД
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('/')
    else:
        form = RegisterUserForm()
    return render(request, 'task_mastery/register.html', {'form': form})
    
    
def logout_user(request):
    logout(request)
    return redirect('/')


@login_required    
def account(request):

    months = [
        "Января",
        "Февраля",
        "Марта",
        "Апреля",
        "Мая",
        "Июня",
        "Июля",
        "Августа",
        "Сентября",
        "Октября",
        "Ноября",
        "Декабря"
    ]

    days = [
            "Понедельник",
            "Вторник",
            "Среда",
            "Четверг",
            "Пятница",
            "Суббота",
            "Воскресенье",
        ]

    current_date = datetime.date.today()
    day_week = current_date.today().weekday()
    current_time = datetime.datetime.now().strftime("%H")

    if int(current_time) >= 0 and int(current_time) < 5:
        greetings = 'Доброй ночи'
    elif int(current_time) > 5 and int(current_time) < 12:
        greetings = 'Доброе утро'
    else:
        greetings = 'Добрый вечер'


    for i in range(len(months)):
        if i == current_date.month - 1:
            date = months[i]

    for i in range(len(days)):
            if day_week == i:
                day_week = days[i]


    user = request.user

    return render(request, 'task_mastery/cabinet.html', {"current_date": f"{day_week}, {current_date.day} {date}", "user": user, "greetings": greetings})

# class Account(LoginRequiredMixin, DataMixin, DetailView):
#     template_name = 'task_mastery/cabinet.html'

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="TaskMastery")
#         return dict(list(context.items()) + list(c_def.items()))


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'task_mastery/index.html' 
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TaskMastery")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('task_mastery:account')
    
    def form_invalid(self, form):
        messages.error(self.request,'Неверный логин или пароль')
        return self.render_to_response(self.get_context_data(form=form))
    