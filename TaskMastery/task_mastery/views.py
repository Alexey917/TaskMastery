from django.shortcuts import render
from django.views.generic import CreateView

from django.urls import reverse_lazy
from .utils import DataMixin
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.views import LoginView


def index(request, *args, **kwargs):
    if 'password2' in request.POST:
        return RegisterUser.as_view()(request)
    return LoginUser.as_view()(request)
                  

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'task_mastery/base.html' 
    success_url = reverse_lazy('account') 

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TaskMastery")
        return dict(list(context.items()) + list(c_def.items()))
    

    
    
    
def account(request):
    return render(request, 'task_mastery/account.html')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'task_mastery/base.html' 
 
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="TaskMastery")
        return dict(list(context.items()) + list(c_def.items()))
    
    def get_success_url(self):
        return reverse_lazy('account')