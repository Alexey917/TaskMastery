from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy, reverse
from .utils import DataMixin
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView


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


# class RegisterUser(DataMixin, CreateView):
#     form_class = RegisterUserForm
#     template_name = 'task_mastery/register.html' 
#     success_url = reverse_lazy('/') 

#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title="TaskMastery")
#         return dict(list(context.items()) + list(c_def.items()))
    
    
    

    
def account(request):
    return render(request, 'task_mastery/account.html')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'task_mastery/index.html' 
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TaskMastery")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('account')