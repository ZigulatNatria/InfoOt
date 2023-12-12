from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView
from info.models import Employee
from .forms import UserAddForm


class UserAddView(PermissionRequiredMixin, CreateView):
    permission_required = (
        'info.employee.add_employee',
    )
    model = Employee
    template_name = 'create.html'
    form_class = UserAddForm