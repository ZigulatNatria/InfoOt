from django.urls import path
from .views import EmployeeListVew, profile_employee, medicine,\
    certificate, psycho, education, EmployeeUpdateView, CertificateUpdateView, EducationUpdateView, \
    MedicineParagraphUpdateView, EmployeeAddView, PassportAddView, PassportUpdateView, MedicineAddView, \
    MedicineParagraphAddView, EducationAddView, CertificateAddView
urlpatterns = [
    path('', EmployeeListVew.as_view(), name='employee'),
    path('<int:employee_id>/', profile_employee, name='profile_employee'),
    path('medicine/<int:medicine_id>', medicine, name='medicine'),
    path('certificate/<int:employee_id>', certificate, name='certificate'),
    path('psycho/<int:employee_id>', psycho, name='psycho'),
    path('education/<int:employee_id>', education, name='education'),
    #Редактирование
    path('employee_update/<pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('certificate_update/<pk>/', CertificateUpdateView.as_view(), name='certificate_update'),
    path('education_update/<pk>/', EducationUpdateView.as_view(), name='education_update'),
    path('paragraph_update/<pk>/', MedicineParagraphUpdateView.as_view(), name='paragraph_update'),
    path('passport_update/<pk>/', PassportUpdateView.as_view(), name='passport_update'),
    #Добавление
    path('employee_add/', EmployeeAddView.as_view(), name='employee_add'),
    path('passport_add/', PassportAddView.as_view(), name='passport_add'),
    path('medicine_add/', MedicineAddView.as_view(), name='medicine_add'),
    path('paragraph_add/', MedicineParagraphAddView.as_view(), name='paragraph_add'),
    path('education_add/', EducationAddView.as_view(), name='education_add'),
    path('certificate_add/', CertificateAddView.as_view(), name='certificate_add'),
]