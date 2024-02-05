from django import forms

from .models import Employee, Medicine, MedicineParagraph, Certificate, MedicineParagraphList
import datetime
from django.db.models import Q


def employ_list_medicine(name_paragraph: str, days: int) -> set:
    """
    Функция выбирает нужные мед.осмотры с датой (текущий день + <нужное кол-во дней>)
    функция возвращает множество из id работников с подходящими мед.осмотрами
    """
    month_day = datetime.date.today() + datetime.timedelta(days=days)  # вычисляем 15 дней от текущей даты
    list_id = []
    try:
        id_name_paragraph_list = MedicineParagraphList.objects.get(number_paragraph=name_paragraph).id
        employ_id = MedicineParagraph.objects.filter(Q(number_paragraph_list=id_name_paragraph_list) &
                                                     Q(date_end_paragraph__gt=month_day)).values('medicine__employee')
        for i in employ_id:
            list_id.append(i['medicine__employee'])

        return set(list_id)      #преобразуем полученный список id во множество
    except BaseException:
        print('Отсутствует соответсвующий пункт мед.осмотра в базе')
        return set({})


def employ_list_certificate(certificate_name: str, days: int) -> set:
    """
    Функция выбирает нужные удостоверения с датой (текущий день + <нужное кол-во дней>)
    функция возвращает множество из id работников с подходящими удостоверениями
    """
    month_day = datetime.date.today() + datetime.timedelta(days=days)  # вычисляем 15 дней от текущей даты
    list_id = []
    try:
        certificates = Certificate.objects.filter(Q(name_certificate_list__name_certificate=certificate_name) &
                                                  Q(date_end_certificate__gt=month_day)).values('employee')
        for i in certificates:
            list_id.append(i['employee'])
        return set(list_id)          #преобразуем полученный список id во множество
    except BaseException:
        print('Отсутствует соответсвующее обучение в базе')
        return set({})


def employ_list_height(employ_certificate: set, employ_medicine: set):
    """производим пересечение множеств id, функция возвращает кверисет"""
    employs_id = employ_certificate & employ_medicine
    employs = Employee.objects.filter(id__in=employs_id)   #фильтрация по id
    return employs


class PdfTestForm(forms.Form):
    text = forms.CharField(max_length=255)
    """конструктор для обновления формы"""
    def __init__(self, *args, **kwargs):
        super(PdfTestForm, self).__init__(*args, **kwargs)
        self.fields['employee'] = forms.ModelMultipleChoiceField(
            queryset=employ_list_height(
                employ_list_certificate('Высота 2 группа', 15),
                employ_list_medicine('6.1', 15)
            )
        )
        self.fields['employee_supervisor'] = forms.ModelMultipleChoiceField(
            queryset=employ_list_height(
                employ_list_certificate('Высота 3 группа', 15),
                employ_list_medicine('6.2', 15)
            )
        )

