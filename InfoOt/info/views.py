from django.shortcuts import render
from .models import Employee, Passport, Education, Certificate, Psycho, Medicine, MedicineParagraph
from django.views.generic import ListView

# Create your views here.
class EmployeeListVew(ListView):
    model = Employee
    context_object_name = 'employee'
    template_name = 'index.html'
    queryset = Employee.objects.all()


def profile_employee(request, employee_id):
    education = Education.objects.get(pk=employee_id)
    passport = Passport.objects.get(pk=employee_id)
    current_profile = Employee.objects.get(pk=employee_id)
    psycho = Psycho.objects.get(pk=employee_id)
    medicine = Medicine.objects.get(employee=employee_id) #обращаемся к полю медицины через связанную модель Employee
    context = {'education': education, 'passport': passport, 'current_profile': current_profile,
               'certificate': certificate, 'psycho': psycho, 'medicine': medicine,
               }
    return render(request, 'profile.html', context)


def medicine(request, medicine_id):
    medicineParagraph = MedicineParagraph.objects.filter(medicine=medicine_id) #обращемся к полю параграф через связанную модель медицины
    context = {'medicineParagraph': medicineParagraph, 'medicine': medicine}
    return render(request, 'medicine.html', context)


def certificate(request, employee_id):
    cer = Certificate.objects.filter(employee=employee_id)
    context = {'cer': cer}
    return render(request, 'certificate.html', context)