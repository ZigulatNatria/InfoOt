from django.db import models
from PIL import Image #импорт из PILLOW для обращения к изображению
import datetime

# Create your models here.
class Employee(models.Model):
    surname = models.CharField(max_length=100, verbose_name='Фамилия')
    name = models.CharField(max_length=100, verbose_name='Имя')
    patronym = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения')
    phone = models.IntegerField(verbose_name='Телефон')
    subdivision = models.CharField(max_length=150, verbose_name='Подразделение')
    photo_employee = models.ImageField(verbose_name='Фото работника', null=True, blank=True)
    profession = models.TextField(verbose_name='Профессия')

#Функция для преобразования загружаемой картинки к нужному размеру
    # def save(self):
    #     super().save()
    #     img = Image.open(self.photo_employee.path)
    #
    #     if img.height > 100 or img.width > 100:
    #         output_size = (100, 100)
    #         img.thumbnail(output_size)
    #         img.save(self.photo_employee.path)

    def __str__(self):
        return '{}'.format(self.surname) + ' ' + '{}'.format(self.name) + ' ' + '{}'.format(self.patronym)

    class Meta:
        verbose_name_plural = 'Работник'
        verbose_name = 'Работники'


class Passport(models.Model):
    series = models.IntegerField(verbose_name='Серия')
    number = models.IntegerField(verbose_name='Номер')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    fms = models.TextField(verbose_name='Кем выдан')
    registration = models.TextField(verbose_name='Регистрация')
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Паспорт' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Паспорт'
        verbose_name = 'Паспорта'


class Education(models.Model):
    prof_name = models.TextField(verbose_name='Нзвание специальноости')
    date_finish_education = models.DateField(verbose_name='Дата окончания уч.заведения')
    document_education = models.FileField(verbose_name='Скан документа', null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Образование' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Образование'
        verbose_name = 'Образования'


class Certificate(models.Model):
    name_certificate = models.TextField(verbose_name='Название обучения')
    date_finish_certificate = models.DateField(verbose_name='Дата получения удостоверения')
    date_end_certificate = models.DateField(verbose_name='Срок окончания действия удостоверения')
    certificate = models.FileField(verbose_name='Скан удостоверения', upload_to='media', null=True, blank=True)
    protocol = models.FileField(verbose_name='Скан протокола', upload_to='media', null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Удостоверение ' + ' ' + '{}'.format(self.name_certificate) + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Удостоверение'
        verbose_name = 'Удостоверения'

    # расчитываем колличество дней до окончания срока действия, берём дату окончания из модели и вычитаем текущую дату
    def time(self):
        return (self.date_end_certificate - datetime.date.today()).days


class Psycho(models.Model):
    date_finish_psycho = models.DateField(verbose_name='Дата прохождения освидетельствования')
    date_end_psycho = models.DateField(verbose_name='Срок действия освидетельствования')
    photo_psycho = models.ImageField(verbose_name='Скан освидетельствования')
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Псих.освидетельствование' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Псих.освидетельстование'
        verbose_name = 'Псих.освидетельствования'


class Medicine(models.Model):
    photo_medicine = models.ImageField(verbose_name='Скан мед.заключения')
    date_medicine = models.DateField(verbose_name='Дата прохождения мед.комиссии')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Мед.заключение' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Мед.заключение'
        verbose_name = 'Мед.заключения'


class MedicineParagraph(models.Model):
    number_paragraph = models.CharField(max_length=10, verbose_name='Пункт мед.осмотра')
    date_finish_paragraph = models.DateField(verbose_name='Дата прохождения')
    date_end_paragraph = models.DateField(verbose_name='Срок действия')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Мед.заключение')

    def __str__(self):
        return 'Пункт' + ' ' + '{}'.format(self.number_paragraph) + ' ' + '{}'.format(self.medicine)

    class Meta:
        verbose_name_plural = 'Пункт мед.осмотра'
        verbose_name = 'Пункты мед.осмотра'

