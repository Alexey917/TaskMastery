from .forms import RegisterUserForm, LoginUserForm

planning = [
  'систематизируйте свои проекты', 
  'создавайте четкие планы действий', 
  'отслеживайте прогресс в реальном времени'
]
    
siteIntended = [
  'повысить свою продуктивность',
  'легко планировать и отслеживать свои дела',
  'а также эффективно координировать работу в команде'
]

teamWork = [
  'работайте с коллегами над общими проектами',
  'делегируйте задачи',
  'обменивайтесь комментариями и файлами для более эффективного сотрудничества'
]


class DataMixin:
  def get_user_context(self, **kwargs):
    context = kwargs
    context['planning'] = planning
    context['siteIntended'] = siteIntended
    context['teamWork'] = teamWork
    # context['formReg'] = RegisterUserForm
    # context['formAuth'] = LoginUserForm
    return context