from django.shortcuts import render


# Create your views here.
def index(request):
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

    return render(request, 'task_mastery/base.html', context={"planning": planning, 
                                                              "siteIntended": siteIntended,
                                                              "teamWork": teamWork})

