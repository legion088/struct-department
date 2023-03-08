from django.shortcuts import render
from .models import *


def start_home_page(request):
    context = {
        'department': Department.objects.all(),
        'type': TypeProgram.objects.all(),
        'programs': Programs.objects.all(),
        'disciplines': Disciplines.objects.all(),
    }

    return render(request,
                  template_name='struct_department/index.html',
                  context=context)
