from django.shortcuts import render
from .models import Employee, Passport, Education, Certificate, Psycho, Medicine, MedicineParagraph
from django.views.generic import ListView, UpdateView, CreateView, View
from .forms import EmployeeAddForm, CertificateAddForm, EducationAddForm, MedicineParagraphAddForm, \
    PassportAddForm, MedicineAddForm, PsychoAddForm
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
    psycho = Psycho.objects.filter(employee=employee_id)
    passport = Passport.objects.filter(employee=employee_id)
    current_profile = Employee.objects.get(pk=employee_id)
    medicine = Medicine.objects.filter(employee=employee_id) #обращаемся к полю медицины через связанную модель Employee
    # medicine_paragraph = MedicineParagraph.objects.filter(employee=medicine.id)
    context = {'passport': passport,
               'current_profile': current_profile,
               'certificate': certificate,
               'medicine': medicine,
               'education': education,
               'psycho': psycho,
               # 'medicine_paragraph': medicine_paragraph
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


"""Информация о сроках"""
def time_out(request):
    month = datetime.date.today() + datetime.timedelta(days=30)

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
        'psycho_month': psycho_month
    }
    return render(request, 'time_out.html', context)


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