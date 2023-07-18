from django.shortcuts import render
from .models import Employee, Passport, Education, Certificate, Psycho, Medicine, MedicineParagraph, Subdivision, Sawc
from django.views.generic import ListView, UpdateView, CreateView, View, TemplateView, DeleteView
from .forms import EmployeeAddForm, CertificateAddForm, EducationAddForm, MedicineParagraphAddForm, \
    PassportAddForm, MedicineAddForm, PsychoAddForm, SawcAddForm, SawcAddToEmployeeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
import datetime


"""Временно закрыто"""
#для Celery
# from .tasks import certificate_created, send_test_email
# from .service import send

#для PDF
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from .utils import render_to_pdf
# from .utils import render_pdf
from django.http import HttpResponse


"""Работник"""
class EmployeeView(LoginRequiredMixin, TemplateView):
    template_name = 'employee_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        set_subdivision_employee = {subdivision: subdivision.employee_set.all()
                                    for subdivision in Subdivision.objects.all().prefetch_related('employee_set')}
        context['all_employee_by_subdivision'] = set_subdivision_employee
        return context


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create.html'
    form_class = EmployeeAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Employee.objects.get(pk=id)


class EmployeeAddView(LoginRequiredMixin, CreateView):
    model = Employee
    template_name = 'create.html'
    form_class = EmployeeAddForm


def profile_employee(request, employee_id):
    education = Education.objects.filter(employee=employee_id)
    certificate = Certificate.objects.filter(employee=employee_id)
    psycho = Psycho.objects.filter(employee=employee_id)
    passport = Passport.objects.filter(employee=employee_id)
    current_profile = Employee.objects.get(pk=employee_id)
    try:
        medicine = Medicine.objects.get(employee=employee_id) #обращаемся к полю медицины через связанную модель Employee
        medicine_paragraph = MedicineParagraph.objects.filter(medicine=medicine.id)
    except Exception:
        medicine = []
        medicine_paragraph = []
    # medicine_paragraph = MedicineParagraph.objects.filter(medicine=medicine.id)
    context = {'passport': passport,
               'current_profile': current_profile,
               'certificate': certificate,
               'medicine': medicine,
               'education': education,
               'psycho': psycho,
               'medicine_paragraph': medicine_paragraph
               }
    return render(request, 'profile.html', context)


class SawcAddToEmployee(LoginRequiredMixin, UpdateView):
    template_name = 'create.html'
    form_class = SawcAddToEmployeeForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Employee.objects.get(pk=id)


"""Паспорт"""
class PassportAddView(LoginRequiredMixin, CreateView):
    model = Passport
    template_name = 'create.html'
    form_class = PassportAddForm


class PassportUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create.html'
    form_class = PassportAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Passport.objects.get(pk=id)

"""Медицина"""
def medicine(request, medicine_id):
    medicine = Medicine.objects.get(id=medicine_id)
    medicineParagraph = MedicineParagraph.objects.filter(medicine=medicine_id) #обращемся к полю параграф через связанную модель медицины
    context = {'medicineParagraph': medicineParagraph, 'medicine': medicine}
    return render(request, 'medicine.html', context)


class MedicineParagraphUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create.html'
    form_class = MedicineParagraphAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return MedicineParagraph.objects.get(pk=id)


class MedicineAddView(LoginRequiredMixin, CreateView):
    model = Medicine
    template_name = 'create.html'
    form_class = MedicineAddForm


class MedicineParagraphAddView(LoginRequiredMixin, CreateView):
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


class CertificateUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create.html'
    form_class = CertificateAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Certificate.objects.get(pk=id)


class CertificateAddView(LoginRequiredMixin, CreateView):
    model = Certificate
    template_name = 'create.html'
    form_class = CertificateAddForm


"""Временно закрыто"""
#Для Celery
    # def form_valid(self, form):
    #     form.save()
    #     # send('ZigulatNatria@yandex.ru')
    #     send_test_email.delay('ZigulatNatria@yandex.ru')
    #     return super().form_valid(form)


"""Психиатрия"""
def psycho(request, employee_id):
    psycho = Psycho.objects.filter(employee=employee_id)
    context = {'psycho': psycho}
    return render(request, 'psycho.html', context)


class PsychoAddView(LoginRequiredMixin, CreateView):
    model = Psycho
    template_name = 'create.html'
    form_class = PsychoAddForm


class PsychoUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create.html'
    form_class = PsychoAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Psycho.objects.get(pk=id)


"""Образование"""
def education(request, employee_id):
    education = Education.objects.filter(employee=employee_id)
    context = {'education': education}
    return render(request, 'education.html', context)


class EducationUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create.html'
    form_class = EducationAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Education.objects.get(pk=id)


class EducationAddView(LoginRequiredMixin, CreateView):
    model = Education
    template_name = 'create.html'
    form_class = EducationAddForm


"""Информация о сроках"""
def time_out(request):
    month = datetime.date.today() + datetime.timedelta(days=30)
    current_user = request.user
    subdivision_current_user = current_user.subdivision
    employee_in_subdivision = Employee.objects.filter(subdivision=subdivision_current_user)
    set_subdivision_certificate = {employee: employee.certificate_set.filter(date_end_certificate__lte=datetime.date.today())
                                   for employee in Employee.objects.filter(subdivision=subdivision_current_user).prefetch_related('certificate_set')}
    set_subdivision_certificate_month = {
        employee: employee.certificate_set.filter(date_end_certificate__range=(datetime.date.today(), month))
        for employee in
        Employee.objects.filter(subdivision=subdivision_current_user).prefetch_related('certificate_set')}

    # print(current_user)
    # print(subdivision_current_user)
    # # print(employee_in_subdivision)
    # print(set_subdivision_certificate)
    # print(set_subdivision_certificate_month)

    certificate = Certificate.objects.filter(date_end_certificate__lte=datetime.date.today())
    certificate_month = Certificate.objects.filter(date_end_certificate__range=(datetime.date.today(), month))

    medicine = MedicineParagraph.objects.filter(date_end_paragraph__lte=datetime.date.today())
    medicine_month = MedicineParagraph.objects.filter(date_end_paragraph__range=(datetime.date.today(), month))

    psycho = Psycho.objects.filter(date_end_psycho__lte=datetime.date.today())
    psycho_month = Psycho.objects.filter(date_end_psycho__range=(datetime.date.today(), month))
    context = {
        'certificate': certificate,
        'certificate_month': certificate_month,
        'medicine': medicine,
        'medicine_month': medicine_month,
        'psycho': psycho,
        'psycho_month': psycho_month,
        'set_subdivision_certificate': set_subdivision_certificate,
        'set_subdivision_certificate_month': set_subdivision_certificate_month,
    }
    return render(request, 'time_out_subdivision.html', context)


"""СОУТ"""
class SawcAddView(LoginRequiredMixin, CreateView):
    model = Sawc
    template_name = 'create.html'
    form_class = SawcAddForm


class SawcListView(LoginRequiredMixin, ListView):
    model = Sawc
    template_name = 'sawc_list.html'
    context_object_name = 'sawc_list'


class SawcDelete(LoginRequiredMixin, DeleteView):
    queryset = Sawc.objects.all()
    context_object_name = 'sawc'
    template_name = 'delete/sawc_delete.html'
    success_url = '/sawc/'


class SawcUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'create.html'
    form_class = SawcAddForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Sawc.objects.get(pk=id)


"""PDF пробный запуск"""
def some_view(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Привет мир.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         pdf = render_to_pdf('pdf/report.html')
#         return HttpResponse(pdf, content_type='application/pdf')


class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        employee_ = Employee.objects.get(id=1)
        employee_name = employee_.name
        data = {
        "name": employee_name, #you can feach the data from database
        "id": 18,
        "amount": 333,
        }
        pdf = render_to_pdf('pdf/report.html', data)
        # pdf = render_pdf('pdf/report.html', data)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Report_for_%s.pdf" %(data['id'])
            content = "inline; filename= %s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Page Not Found")


def index(request):
    return render(request, 'pdf/report.html')