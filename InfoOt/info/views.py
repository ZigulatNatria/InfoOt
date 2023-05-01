from django.shortcuts import render
from .models import Employee, Passport, Education, Certificate, Psycho, Medicine, MedicineParagraph
from django.views.generic import ListView, UpdateView, CreateView
from .forms import EmployeeAddForm, CertificateAddForm, EducationAddForm, MedicineParagraphAddForm, \
    PassportAddForm, MedicineAddForm, PsychoAddForm
from django.utils import timezone
import datetime

#для Celery
from .tasks import certificate_created, send_test_email
from .service import send


"""Работник"""
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


class EmployeeAddView(CreateView):
    model = Employee
    template_name = 'create.html'
    form_class = EmployeeAddForm


def profile_employee(request, employee_id):
    education = Education.objects.filter(employee=employee_id)
    certificate = Certificate.objects.filter(employee=employee_id)
    passport = Passport.objects.filter(employee=employee_id)
    current_profile = Employee.objects.get(pk=employee_id)
    medicine = Medicine.objects.filter(employee=employee_id) #обращаемся к полю медицины через связанную модель Employee
    context = {'passport': passport,
               'current_profile': current_profile,
               'certificate': certificate,
               'medicine': medicine,
               'education': education
               }
    return render(request, 'profile.html', context)


"""Паспорт"""
class PassportAddView(CreateView):
    model = Passport
    template_name = 'create.html'
    form_class = PassportAddForm


class PassportUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = PassportAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Passport.objects.get(pk=id)


def medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    medicineParagraph = MedicineParagraph.objects.filter(medicine=medicine_id) #обращемся к полю параграф через связанную модель медицины
    context = {'medicineParagraph': medicineParagraph, 'medicine': medicine}
    return render(request, 'medicine.html', context)


class MedicineParagraphUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = MedicineParagraphAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return MedicineParagraph.objects.get(pk=id)


class MedicineAddView(CreateView):
    model = Medicine
    template_name = 'create.html'
    form_class = MedicineAddForm


class MedicineParagraphAddView(CreateView):
    model = MedicineParagraph
    template_name = 'create.html'
    form_class = MedicineParagraphAddForm


"""Обучение"""
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


class CertificateUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = CertificateAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Certificate.objects.get(pk=id)


class CertificateAddView(CreateView):
    model = Certificate
    template_name = 'create.html'
    form_class = CertificateAddForm

#Для Celery

    def form_valid(self, form):
        form.save()
        # send('ZigulatNatria@yandex.ru')
        send_test_email.delay('ZigulatNatria@yandex.ru')
        return super().form_valid(form)


"""Психиатрия"""
def psycho(request, employee_id):
    psycho = Psycho.objects.filter(employee=employee_id)
    context = {'psycho': psycho}
    return render(request, 'psycho.html', context)


"""Образование"""
def education(request, employee_id):
    education = Education.objects.filter(employee=employee_id)
    context = {'education': education}
    return render(request, 'education.html', context)


class EducationUpdateView(UpdateView):
    template_name = 'create.html'
    form_class = EducationAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Education.objects.get(pk=id)


class EducationAddView(CreateView):
    model = Education
    template_name = 'create.html'
    form_class = EducationAddForm


class PsychoAddView(CreateView):
    model = Psycho
    template_name = 'create.html'
    form_class = PsychoAddForm