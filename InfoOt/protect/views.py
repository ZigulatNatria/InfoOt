from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from info.models import Employee, Education, Medicine, MedicineParagraph, Certificate


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_aut'] = self.request.user.groups.exists()
        return context

    def employee_id(self):
        employee_id = self.request.user.id
        return employee_id

    def employee(self):
        current_profile = Employee.objects.get(pk=self.employee_id())
        return current_profile

    def education(self):
        education = Education.objects.filter(employee=self.employee_id())
        return education

    def medicine(self):
        try:
            medicine = Medicine.objects.get(
                employee=self.employee_id())
        except Exception:
            medicine = []
        return medicine

    def medicine_paragraph(self):
        try:
            medicine = self.medicine
            medicine_paragraph = MedicineParagraph.objects.filter(medicine=medicine.id)
        except Exception:
            medicine_paragraph = []
        return medicine_paragraph

    def certificate(self):
        certificate = Certificate.objects.filter(employee=self.employee_id())
        return certificate


    # def profile_employee(request, employee_id):
    #     education = Education.objects.filter(employee=employee_id)
    #     certificate = Certificate.objects.filter(employee=employee_id)
    #     psycho = Psycho.objects.filter(employee=employee_id)
    #     passport = Passport.objects.filter(employee=employee_id)
    #     current_profile = Employee.objects.get(pk=employee_id)
    #     try:
    #         medicine = Medicine.objects.get(
    #             employee=employee_id)  # обращаемся к полю медицины через связанную модель Employee
    #         medicine_paragraph = MedicineParagraph.objects.filter(medicine=medicine.id)
    #     except Exception:
    #         medicine = []
    #         medicine_paragraph = []
    #
    #     context = {'passport': passport,
    #                'current_profile': current_profile,
    #                'certificate': certificate,
    #                'medicine': medicine,
    #                'education': education,
    #                'psycho': psycho,
    #                'medicine_paragraph': medicine_paragraph
    #                }
    #     return render(request, 'profile.html', context)