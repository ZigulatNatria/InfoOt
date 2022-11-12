from django.db import models

# Create your models here.
class Employee(models.Model):
    surname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    patronym = models.CharField(max_length=100, null=True)
    birth_date = models.DateField()
    phone = models.IntegerField()
    subdivision = models.CharField(max_length=150)
    photo_employee = models.ImageField(null=True)
    profession = models.TextField()

    def __str__(self):
        return '{}'.format(self.surname) + ' ' + '{}'.format(self.name) + ' ' + '{}'.format(self.patronym)

    class Meta:
        verbose_name_plural = 'Работник'
        verbose_name = 'Работники'


class Passport(models.Model):
    series = models.IntegerField()
    number = models.IntegerField()
    date_of_issue = models.DateField()
    fms = models.TextField()
    registration = models.TextField()
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return 'Паспорт' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Паспорт'
        verbose_name = 'Паспорта'


class Education(models.Model):
    prof_name = models.TextField()
    date_finish_education = models.DateField()
    photo_education = models.ImageField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return 'Образование' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Образование'
        verbose_name = 'Образования'


class Certificate(models.Model):     #TODO добавить в модель поле для фото протокола
    name_certificate = models.TextField()
    date_finish_certificate = models.DateField()
    date_end_certificate = models.DateField()
    photo_certificate = models.ImageField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return 'Удостоверение ' + ' ' + '{}'.format(self.name_certificate) + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Удостоверение'
        verbose_name = 'Удостоверения'


class Psycho(models.Model):
    date_finish_psycho = models.DateField()
    date_end_psycho = models.DateField()
    photo_psycho = models.ImageField()
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return 'Псих.освидетельствование' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Псих.освидетельстование'
        verbose_name = 'Псих.освидетельствования'


class Medicine(models.Model):
    photo_medicine = models.ImageField()
    date_medicine = models.DateField()
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return 'Мед.заключение' + ' ' + '{}'.format(self.employee)

    class Meta:
        verbose_name_plural = 'Мед.заключение'
        verbose_name = 'Мед.заключения'


class MedicineParagraph(models.Model):
    number_paragraph = models.IntegerField()    #TODO Переделать на float
    date_finish_paragraph = models.DateField()
    date_end_paragraph = models.DateField()
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)

    def __str__(self):
        return 'Пункт' + ' ' + '{}'.format(self.number_paragraph) + ' ' + '{}'.format(self.medicine)

    class Meta:
        verbose_name_plural = 'Пункт мед.осмотра'
        verbose_name = 'Пункты мед.осмотра'

