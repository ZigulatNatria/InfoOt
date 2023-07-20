from django.db import models
from django.contrib.auth.models import AbstractUser, User
from PIL import Image #импорт из PILLOW для обращения к изображению
import datetime
import uuid


class Subdivision(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #TODO не хочет работать с функциями view допинать по возможности
    name = models.CharField(max_length=150, verbose_name='Подразделение')

    class Meta:
        verbose_name_plural = 'Подразделение'
        verbose_name = 'Подразделения'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'


class Profession(models.Model):
    name = models.CharField(max_length=150, verbose_name='Профессия')

    class Meta:
        verbose_name_plural = 'Профессия'
        verbose_name = 'Профессии'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}'


class Sawc(models.Model):
    name_profession = models.ForeignKey(Profession, verbose_name='Профессия', on_delete=models.CASCADE, null=True, blank=True)
    name_subdivision = models.ForeignKey(Subdivision, verbose_name='Подразделение', on_delete=models.CASCADE, null=True, blank=True)
    number_card = models.CharField(max_length=100, verbose_name='Номер карты СОУТ')
    date_card = models.DateField(verbose_name='Дата карты СОУТ', null=True, blank=True)
    document_sawc = models.FileField(verbose_name='Скан карты СОУТ', null=True, blank=True)
    date_add = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Карты СОУТ'
        verbose_name = 'Карта СОУТ'
        ordering = ['-date_add']

    def __str__(self):
        return '{}'.format(self.number_card) + ' ' + '{}'.format(self.name_profession) + ', ' + '{}'.format(self.name_subdivision)

    def get_absolute_url(self):
        return f'/sawc/'


class Employee(AbstractUser):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #TODO не хочет работать с функциями view допинать по возможности
    surname = models.CharField(max_length=100, verbose_name='Фамилия', null=True, blank=True)
    name = models.CharField(max_length=100, verbose_name='Имя', null=True, blank=True)
    patronym = models.CharField(max_length=100, verbose_name='Отчество', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Дата рождения', null=True, blank=True)
    phone = models.IntegerField(verbose_name='Телефон', null=True, blank=True)
    subdivision = models.ForeignKey(Subdivision, verbose_name='Подразделение', on_delete=models.CASCADE, null=True, blank=True)
    photo_employee = models.ImageField(verbose_name='Фото работника', null=True, blank=True)
    # profession = models.ManyToManyField(Profession, verbose_name='Профессия', blank=True)
    profession = models.ForeignKey(Profession, verbose_name='Профессия', on_delete=models.CASCADE, null=True, blank=True)
    sawc = models.ManyToManyField(Sawc, verbose_name='СОУТ', blank=True)
    supervisor = models.BooleanField(verbose_name='Рководитель', default=False)

    def get_absolute_url(self):
        return f'/{self.id}'

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
        verbose_name_plural = 'Работники'
        verbose_name = 'Работник'


class Passport(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #TODO не хочет работать с функциями view допинать по возможности
    series = models.IntegerField(verbose_name='Серия')
    number = models.IntegerField(verbose_name='Номер')
    date_of_issue = models.DateField(verbose_name='Дата выдачи')
    fms = models.TextField(verbose_name='Кем выдан')
    registration = models.TextField(verbose_name='Регистрация')
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Паспорт' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Паспорта'
        verbose_name = 'Паспорт'

    def get_absolute_url(self):
        return f'/{self.employee.id}'


class Education(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #TODO не хочет работать с функциями view допинать по возможности
    prof_name = models.TextField(verbose_name='Нзвание специальноости')
    date_finish_education = models.DateField(verbose_name='Дата окончания уч.заведения')
    document_education = models.FileField(verbose_name='Скан документа', null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Образование' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Образования'
        verbose_name = 'Образование'

    def get_absolute_url(self):
        # return f'/education/{self.employee.id}'
        return f'/{self.employee.id}'


class Certificate(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #TODO не хочет работать с функциями view допинать по возможности
    name_certificate = models.TextField(verbose_name='Название обучения')
    date_finish_certificate = models.DateField(verbose_name='Дата получения удостоверения')
    date_end_certificate = models.DateField(verbose_name='Срок окончания действия удостоверения')
    certificate = models.FileField(verbose_name='Скан удостоверения', upload_to='media', null=True, blank=True)
    protocol = models.FileField(verbose_name='Скан протокола', upload_to='media', null=True, blank=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Удостоверение ' + ' ' + '{}'.format(self.name_certificate) + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Удостоверения'
        verbose_name = 'Удостоверение'

    # расчитываем колличество дней до окончания срока действия, берём дату окончания из модели и вычитаем текущую дату
    def time(self):
        return (self.date_end_certificate - datetime.date.today()).days

    def get_absolute_url(self):
        return f'/{self.employee.id}'


class Psycho(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #TODO не хочет работать с функциями view допинать по возможности
    date_finish_psycho = models.DateField(verbose_name='Дата прохождения освидетельствования')
    date_end_psycho = models.DateField(verbose_name='Срок действия освидетельствования')
    document_psycho = models.FileField(verbose_name='Скан заключения', null=True, blank=True)
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Псих.освидетельствование' + ' ' + '{}'.format(self.employee)

    # расчитываем колличество дней до окончания срока действия, берём дату окончания из модели и вычитаем текущую дату
    def time(self):
        return (self.date_end_psycho - datetime.date.today()).days

    def get_absolute_url(self):
        return f'/{self.employee.id}'

    class Meta:
        verbose_name_plural = 'Псих.освидетельстования'
        verbose_name = 'Псих.освидетельствование'


class Medicine(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #TODO не хочет работать с функциями view допинать по возможности
    document_medicine = models.FileField(verbose_name='Скан заключения', null=True, blank=True)
    date_medicine = models.DateField(verbose_name='Дата прохождения мед.комиссии')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник')

    def __str__(self):
        return 'Мед.заключение' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Мед.заключения'
        verbose_name = 'Мед.заключение'

    def get_absolute_url(self):
        return f'/{self.employee.id}'


class MedicineParagraph(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) #TODO не хочет работать с функциями view допинать по возможности
    number_paragraph = models.CharField(max_length=10, verbose_name='Пункт мед.осмотра')
    date_finish_paragraph = models.DateField(verbose_name='Дата прохождения')
    date_end_paragraph = models.DateField(verbose_name='Срок действия')
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE, verbose_name='Мед.заключение')

    def __str__(self):
        return 'Пункт' + ' ' + '{}'.format(self.number_paragraph) + ' ' + '{}'.format(self.medicine)

    # расчитываем колличество дней до окончания срока действия, берём дату окончания из модели и вычитаем текущую дату
    def time(self):
        return (self.date_end_paragraph - datetime.date.today()).days

    class Meta:
        verbose_name_plural = 'Пункты мед.осмотра'
        verbose_name = 'Пункт мед.осмотра'

    def get_absolute_url(self):
        return f'/{self.medicine.employee.id}'


class Order(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название приказа')
    number = models.CharField(max_length=10, verbose_name='Номер приказа')
    date = models.DateField(verbose_name='Дата приказа')
    file = models.FileField(verbose_name='Скан приказа', upload_to='media')
    employees = models.ManyToManyField(Employee, verbose_name='Работники в приказе')
    date_add = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Приказы'
        verbose_name = 'Приказ'

    def __str__(self):
        return '{}'.format(self.number) + ' ' + '{}'.format(self.name)

    def get_absolute_url(self):
        return f'/orders/'


class Instruction(models.Model):
    number = models.CharField(max_length=10, verbose_name='Номер инструкции')
    name = models.CharField(max_length=250, verbose_name='Название инструкции')
    date = models.DateField(verbose_name='Дата утверждения инструкции')
    date_end = models.DateField(verbose_name='Срок действия')
    file = models.FileField(verbose_name='Скан инструкции', upload_to='instruction')
    profession = models.ManyToManyField(Profession, verbose_name='Профессия', blank=True)
    employee = models.ManyToManyField(Employee, verbose_name='Работник', blank=True)
    date_add = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Инструкции'
        verbose_name = 'Инструкция'

    def __str__(self):
        return '{}'.format(self.number) + ' ' + '{}'.format(self.name)

    def get_absolute_url(self):
        return f'/instructions/'

