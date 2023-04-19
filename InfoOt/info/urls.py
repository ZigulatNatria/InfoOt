from django.urls import path
from .views import EmployeeListVew, profile_employee, medicine,\
    certificate, psycho, education, EmployeeUpdateView, CertificateUpdateView, EducationUpdateView, \
    МedicineParagraphUpdateView
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
    path('paragraph_update/<pk>/', МedicineParagraphUpdateView.as_view(), name='paragraph_update'),
]