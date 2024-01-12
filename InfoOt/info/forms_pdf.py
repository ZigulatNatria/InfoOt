from django import forms
from .models import Employee, Medicine, MedicineParagraph
import datetime


class PdfTestForm(forms.Form):
    medicine_id = Medicine.objects.all().values('id')[::] # получаем все id мед.осмотров
    print(medicine_id)
    for m_id in medicine_id:        # перебираем все параграфы полученных медосмотров
        # print(m_id['id'])
        medicine_paragraph = MedicineParagraph.objects.filter(medicine=m_id['id']).values_list(
                'number_paragraph',
                'date_end_paragraph',
        )
        paragraph = dict(medicine_paragraph)      # преобразуем кортеж в словарь
        try:
            month_day = datetime.date.today() + datetime.timedelta(days=15)       # вычисляем 15 дней от текущей даты
            if paragraph['6.1'] >= month_day:              # если срок параграфа 6.1 не менее 15 дней
                medicine_paragraph.values()         # то получаем все значения нужного параграфа
                id_medicine_filtered = medicine_paragraph.values('medicine_id')[0]['medicine_id']  # забираем id заключений т.к. в коллекции содержится пункт 6.1 берём любой(первый) элемент коллекции и забираем id заключения
                id_employee_filtered = Medicine.objects.filter(id=id_medicine_filtered).values('employee_id')[0]['employee_id']  # забираем id работиков
                print(Employee.objects.filter(id=id_employee_filtered))    #TODO объединить полученные кверисеты
        except Exception:
            pass

    text = forms.CharField(max_length=255)
    employee = forms.ModelChoiceField(queryset=Employee.objects.all())