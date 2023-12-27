from .models import Employee, Passport, Medicine, MedicineParagraph, Psycho, Certificate
from django.http import HttpResponse
import xlwt
from transliterate import translit, get_available_language_codes


def export_users_xls(request, employee_id):
    employee_name = Employee.objects.get(id=employee_id).surname
    trans_name = translit(employee_name, language_code='ru', reversed=True)
    file_name = f"{trans_name}.xls"
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename={file_name}'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Employee')

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style_bold = xlwt.easyxf('font: bold on', )

    columns_employee = [
        'Фамилия',
        'Имя',
        'Отчество',
        'Дата рождения',
        'Профессия',
        'Подразделение',
        'телефон',
    ]

    columns_passport = [
        'Серия',
        'Номер',
        'Дата выдачи',
        'Кем выдан',
        'Регистрация',
    ]

    columns_medicine = [
        'Номер пункта',
        'Дата мед.осмотра',
        'Срок действия',
    ]

    columns_psycho = [
        'Дата заключения',
        'Срок действия',
    ]

    columns_certificate = [
        'Название обучения',
        'Дата обучения',
        'Срок действия',
    ]

    for col_num in range(len(columns_employee)):
        ws.write(row_num, col_num, columns_employee[col_num], font_style_bold)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    employee = Employee.objects.filter(id=employee_id).values_list(
        'surname',
        'name',
        'patronym',
        'birth_date',
        'profession__name',
        'subdivision__name',
        'phone',
    )
    passport = Passport.objects.filter(employee=employee_id).values_list(
        'series',
        'number',
        'date_of_issue',
        'fms',
        'registration',
    )

    medicine_id = Medicine.objects.filter(employee=employee_id).values('id')[0]['id']
    medicine_paragraph = MedicineParagraph.objects.filter(medicine=medicine_id).values_list(
        'number_paragraph',
        'date_finish_paragraph',
        'date_end_paragraph',
    )

    psycho = Psycho.objects.filter(employee=employee_id).values_list(
        'date_finish_psycho',
        'date_end_psycho',
    )

    certificate = Certificate.objects.filter(employee=employee_id).values_list(
        'name_certificate',
        'date_finish_certificate',
        'date_end_certificate',
    )

    for row in employee:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    row_num += 2
    for col_num in range(len(columns_passport)):
        ws.write(row_num, col_num, columns_passport[col_num], font_style_bold)

    for row in passport:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    row_num += 2
    for col_num in range(len(columns_medicine)):
        ws.write(row_num, col_num, columns_medicine[col_num], font_style_bold)

    for row in medicine_paragraph:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    row_num += 2
    for col_num in range(len(columns_psycho)):
        ws.write(row_num, col_num, columns_psycho[col_num], font_style_bold)

    for row in psycho:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    row_num += 2
    for col_num in range(len(columns_certificate)):
        ws.write(row_num, col_num, columns_certificate[col_num], font_style_bold)

    for row in certificate:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response
