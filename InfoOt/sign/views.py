from django.views.generic.edit import CreateView
from info.models import Employee
from .forms import UserAddForm


class UserAddView(CreateView):
    model = Employee
    template_name = 'create.html'
    form_class = UserAddForm