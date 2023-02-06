from django.shortcuts import render
from .models import Employee, Passport, Education, Certificate, Psycho, Medicine, MedicineParagraph
from django.views.generic import ListView
from django.utils import timezone

# Create your views here.
class EmployeeListVew(ListView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'index.html'
    queryset = Employee.objects.all()


def profile_employee(request, employee_id):
    passport = Passport.objects.filter(employee=employee_id)
    current_profile = Employee.objects.get(pk=employee_id)
    medicine = Medicine.objects.filter(employee=employee_id) #обращаемся к полю медицины через связанную модель Employee
    context = {'passport': passport, 'current_profile': current_profile,
               'certificate': certificate, 'medicine': medicine
               }
    return render(request, 'profile.html', context)


def medicine(request, medicine_id):
    medicineParagraph = MedicineParagraph.objects.filter(medicine=medicine_id) #обращемся к полю параграф через связанную модель медицины
    context = {'medicineParagraph': medicineParagraph, 'medicine': medicine}
    return render(request, 'medicine.html', context)


def certificate(request, employee_id):
    now = timezone.now()
    cer = Certificate.objects.filter(employee=employee_id)
    # for cert in cer:
    #     time = cert.date_end_certificate - now.date
    context = {'cer': cer}
    return render(request, 'certificate.html', context)


def psycho(request, employee_id):
    psycho = Psycho.objects.filter(employee=employee_id)
    context = {'psycho': psycho}
    return render(request, 'psycho.html', context)


def education(request, employee_id):
    education = Education.objects.filter(employee=employee_id)
    context = {'education': education}
    return render(request, 'education.html', context)