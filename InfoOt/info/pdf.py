import io

from django.db.models import Q
from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import CreateView
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .models import Employee, SafeSystems
from .forms_pdf import PdfTestForm


pdfmetrics.registerFont(TTFont('Arial', 'arial.ttf'))


c = canvas.Canvas("example.pdf", pagesize=letter)
c.setFont("Arial", 14)
c.drawString(50, 750, "Строка")
c.save()


def add_pdf(request):
    form = PdfTestForm()
    if request.method == 'POST':
        increment = request.POST.get('text')
        contents = request.POST.get('contents_of_work')
        employee = request.POST.getlist('employee')
        safe_systems = request.POST.getlist('safe_systems')
        employee_supervisor = request.POST.get('employee_supervisor')
        request.session['data'] = increment
        request.session['contents'] = contents
        request.session['safe_systems'] = safe_systems
        request.session['employee'] = employee
        request.session['employee_supervisor'] = employee_supervisor
        button_pdf = True
    else:
        increment = 0
        document = None
        button_pdf = False
    return render(request, 'pdf/test_pdf.html', {'form': form, 'increment': increment, 'button_pdf': button_pdf})


def pdf(request):
    increment = request.session.get('data', None)
    contents = request.session.get('contents', None)
    safe_systems = request.session.get('safe_systems', None)
    employee = request.session.get('employee', None)
    employee_supervisor = request.session.get('employee_supervisor', None)

    employs = Employee.objects.filter(id__in=employee)
    safe_systems = SafeSystems.objects.filter(id__in=safe_systems)
    employs_supervisors = Employee.objects.get(id=employee_supervisor)

    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    p.setFont("Arial", 12)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    string = 0
    p.drawString(5, 800, 'ООО "НПО ПермНефтеГаз" ')
    p.drawString(400, 800, 'Производственный департамент ')
    p.drawString(210, 775, 'Наряд-допуск №__/__ ')
    p.drawString(180, 760, 'На производство работ на высоте')
    p.drawString(5, 740, f'1. Место выполнения работ: {increment}')
    p.drawString(5, 720, f'2. Содержание работ: {contents}')
    p.drawString(5, 700, f'3. Выдан: ТУТ БУДЕТ ДАТА')
    p.drawString(380, 700, f'Действителен до: ТУТ БУДЕТ ДАТА')
    p.drawString(380, 680, f'Продлён до: _______')
    p.drawString(5, 660, f'4. Ответственный руководитель работ:        '
                         f'{employs_supervisors.profession.name}          '
                         f'{employs_supervisors.surname} '
                         f'{employs_supervisors.name} '
                         f'{employs_supervisors.patronym}')
    p.drawString(5, 640, f'5. Ответственный исполнитель работ:        '
                         f'{employs_supervisors.profession.name}          '
                         f'{employs_supervisors.surname} '
                         f'{employs_supervisors.name} '
                         f'{employs_supervisors.patronym}')
    p.drawString(5, 620, f'6. Ответственный за подготовку места проведения работ:  '
                         f'{employs_supervisors.profession.name}  '
                         f'{employs_supervisors.surname} '
                         f'{employs_supervisors.name} '
                         f'{employs_supervisors.patronym}')
    p.drawString(5, 600, '7. Мероприятия по подготовке места проведения работ: Описание мероприятий')
    p.drawString(5, 580, '8. Подготовительные работы выполнены в полном объёме. Место проведения работ подготовлено:')
    p.drawString(300, 560, f'{employs_supervisors.profession.name}  '
                           f'{employs_supervisors.surname} '
                           f'{employs_supervisors.name} '
                           f'{employs_supervisors.patronym}')
    p.drawString(5, 540, '9. Место проведения работ принято. С условиями и объёмом проведения работ ознакомлен:')
    p.drawString(300, 520, f'{employs_supervisors.profession.name}  '
                           f'{employs_supervisors.surname} '
                           f'{employs_supervisors.name} '
                           f'{employs_supervisors.patronym}')
    p.drawString(5, 500, '10. Мероприятия обеспечивающие безопасность проведения работ:')
    p.drawString(10, 480, '10.1. Система обеспечения безопасности работ на высоте:')
    p.drawString(12, 460, 'Удерживающие системы')
    for s_s in safe_systems:
        p.drawString(300, 460-string, f"{s_s.name}")
        string += 20
    # for employ in employs:
    #     p.drawString(10, 785-string, f"{employ.surname} {employ.name} {employ.patronym}")
    #     string += 15
    #

    # p.drawString(10, 780-string, f"{increment}")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")






