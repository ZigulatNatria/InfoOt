from django import forms

from .models import Employee, Medicine, MedicineParagraph
import datetime


def employ_list():
    medicine_id = Medicine.objects.all().values('id')[::]  # получаем все id мед.осмотров
    queryset_list = []
    for m_id in medicine_id:  # перебираем все параграфы полученных медосмотров
        medicine_paragraph = MedicineParagraph.objects.filter(medicine=m_id['id']).values_list(
            'number_paragraph_list__number_paragraph',
            'date_end_paragraph',
        )
        paragraph = dict(medicine_paragraph)  # преобразуем кортеж в словарь
        try:
            month_day = datetime.date.today() + datetime.timedelta(days=15)  # вычисляем 15 дней от текущей даты
            if paragraph['6.1'] >= month_day:  # если срок параграфа 6.1 не менее 15 дней
                medicine_paragraph.values()  # то получаем все значения нужного параграфа
                id_medicine_filtered = medicine_paragraph.values('medicine_id')[0][
                    'medicine_id']  # забираем id заключений т.к. в коллекции содержится пункт 6.1 берём любой(первый) элемент коллекции и забираем id заключения
                id_employee_filtered = Medicine.objects.filter(id=id_medicine_filtered).values('employee_id')[0][
                    'employee_id']  # забираем id работиков
                Employee.objects.filter(id=id_employee_filtered)
                queryset_list.append(Employee.objects.filter(id=id_employee_filtered))
        except Exception:
            pass

    empty_qs = Employee.objects.none()
    for i in queryset_list:
        new_qs = empty_qs.union(i)
        empty_qs = new_qs

    return empty_qs


class PdfTestForm(forms.Form):
    text = forms.CharField(max_length=255)
    employee = forms.ModelMultipleChoiceField(queryset=employ_list())
    """конструктор для обновления формы"""
    def __init__(self, *args, **kwargs):
        super(PdfTestForm, self).__init__(*args, **kwargs)
        self.fields['employee'] = forms.ModelMultipleChoiceField(queryset=employ_list())

