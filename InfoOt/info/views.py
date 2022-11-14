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
    certificate = Certificate.objects.get(pk=employee_id) # не работает по всем т.к. принимает id работника
    psycho = Psycho.objects.get(pk=employee_id)
    medicine = Medicine.objects.get(pk=employee_id)
    context = {'education': education, 'passport': passport, 'current_profile': current_profile,
               'certificate': certificate, 'psycho': psycho, 'medicine': medicine,
               }
    return render(request, 'profile.html', context)


def medicine(request, medicine_id):
    medicineParagraph = MedicineParagraph.objects.filter(medicine=medicine_id) #фильтруем через связанное поле с моделью
    medicine = Medicine.objects.get(pk=medicine_id)
    context = {'medicineParagraph': medicineParagraph, 'medicine': medicine}
    return render(request, 'medicine.html', context)