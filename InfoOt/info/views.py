from django.shortcuts import render
from .models import Employee, Passport, Education, Certificate, Psycho, Medicine, MedicineParagraph
from django.views.generic import ListView, UpdateView
from .forms import EmployeeAddForm
from django.utils import timezone
import datetime

# Create your views here.
class EmployeeListVew(ListView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'index.html'
    queryset = Employee.objects.all()


class EmployeeUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = EmployeeAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Employee.objects.get(pk=id)


def profile_employee(request, employee_id):
    passport = Passport.objects.filter(employee=employee_id)
    current_profile = Employee.objects.get(pk=employee_id)
    medicine = Medicine.objects.filter(employee=employee_id) #обращаемся к полю медицины через связанную модель Employee
    context = {'passport': passport, 'current_profile': current_profile,
               'certificate': certificate, 'medicine': medicine
               }
    return render(request, 'profile.html', context)


def medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    medicineParagraph = MedicineParagraph.objects.filter(medicine=medicine_id) #обращемся к полю параграф через связанную модель медицины
    context = {'medicineParagraph': medicineParagraph, 'medicine': medicine}
    return render(request, 'medicine.html', context)


def certificate(request, employee_id):
    cer = Certificate.objects.filter(employee=employee_id)
    # Для обработки всех значений поля date_end_certificate полученный кверисет пропускаем через цикл for
    # создаём пустой список и в него добавляем полученные значения
    # т.к. кверисет это коллекция объектов в цикле обращаемся к каждому объекту Certificate
    time = []
    for t in cer:
        data = t.date_end_certificate
        data_finish = data - datetime.date.today()  # в этой строке вычитаем текущую дату из полученной
        time.append(data_finish)
    context = {'cer': cer, 'time': time}
    return render(request, 'certificate.html', context)


def psycho(request, employee_id):
    psycho = Psycho.objects.filter(employee=employee_id)
    context = {'psycho': psycho}
    return render(request, 'psycho.html', context)


def education(request, employee_id):
    education = Education.objects.filter(employee=employee_id)
    context = {'education': education}
    return render(request, 'education.html', context)