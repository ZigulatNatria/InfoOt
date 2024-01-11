import io
from django.http import FileResponse
from django.shortcuts import render
from django.views.generic import CreateView
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from .models import Employee
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
        employee = request.POST.get('employee')
        request.session['data'] = increment
        request.session['employee'] = employee
    else:
        increment = 0
        document = None
    return render(request, 'pdf/test_pdf.html', {'form': form, 'increment': increment})


def pdf(request):
    increment = request.session.get('data', None)
    employ = Employee.objects.get(id=request.session.get('employee', None))
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)
    p.setFont("Arial", 12)
    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(10, 800, f"{employ.surname} {employ.name} {employ.patronym} {increment}")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")





