from django.urls import path
from .views import profile_employee, medicine,\
    certificate, psycho, education, EmployeeUpdateView, CertificateUpdateView, EducationUpdateView, \
    MedicineParagraphUpdateView, EmployeeAddView, PassportAddView, PassportUpdateView, MedicineAddView, \
    MedicineParagraphAddView, EducationAddView, CertificateAddView, PsychoAddView, EmployeeView,\
    PsychoUpdateView, SawcAddView, SawcAddToEmployee, SawcListView, SawcDelete, SawcUpdateView, OrderListView, \
    OrderAddView, OrderUpdateView, OrderDeleteView, InstructionListView, InstructionCreateView, InstructionUpdateView,\
    InstructionReferenceList, InstructionDeleteView, CertificateCheckView, MedicineParagraphCheckView, PsychoCheckView, \
    time_out, time_out_for_admin, add_familiarization_instruction, search
from .exel import export_users_xls
from .pdf import pdf, add_pdf

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee'),
    path('sawc/', SawcListView.as_view(), name='sawc'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('instructions/', InstructionListView.as_view(), name='instructions'),
    path('<int:employee_id>/', profile_employee, name='profile_employee'),
    path('medicine/<int:medicine_id>', medicine, name='medicine'),
    path('certificate/<int:employee_id>', certificate, name='certificate'),
    path('psycho/<int:employee_id>', psycho, name='psycho'),
    path('education/<int:employee_id>', education, name='education'),
    #Редактирование
    path('employee_update/<pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('certificate_update/<pk>/', CertificateUpdateView.as_view(), name='certificate_update'),
    path('status_update/<pk>', CertificateCheckView.as_view(), name='certificate_check'),
    path('education_update/<pk>/', EducationUpdateView.as_view(), name='education_update'),
    path('paragraph_update/<pk>/', MedicineParagraphUpdateView.as_view(), name='paragraph_update'),
    path('paragraph_status_update/<pk>/', MedicineParagraphCheckView.as_view(), name='medicine_check'),
    path('passport_update/<pk>/', PassportUpdateView.as_view(), name='passport_update'),
    path('psycho_update/<pk>/', PsychoUpdateView.as_view(), name='psycho_update'),
    path('psycho_status_update/<pk>/', PsychoCheckView.as_view(), name='psycho_check'),
    path('sawc_add_to/<pk>', SawcAddToEmployee.as_view(), name='sawc_add_to'),
    path('sawc_update/<pk>', SawcUpdateView.as_view(), name='sawc_update'),
    path('order_update/<pk>', OrderUpdateView.as_view(), name='order_update'),
    path('instruction_update/<pk>', InstructionUpdateView.as_view(), name='instruction_update'),
    #Добавление
    path('employee_add/', EmployeeAddView.as_view(), name='employee_add'),
    path('passport_add/', PassportAddView.as_view(), name='passport_add'),
    path('medicine_add/', MedicineAddView.as_view(), name='medicine_add'),
    path('paragraph_add/', MedicineParagraphAddView.as_view(), name='paragraph_add'),
    path('education_add/', EducationAddView.as_view(), name='education_add'),
    path('certificate_add/', CertificateAddView.as_view(), name='certificate_add'),
    path('psycho_add/', PsychoAddView.as_view(), name='psycho_add'),
    path('sawc_add/', SawcAddView.as_view(), name='sawc_add'),
    path('order_add/', OrderAddView.as_view(), name='order_add'),
    path('instruction_add/', InstructionCreateView.as_view(), name='instruction_add'),
    #Удаление
    path('sawc_delete/<pk>', SawcDelete.as_view(), name='sawc_delete'),
    path('order_delete/<pk>', OrderDeleteView.as_view(), name='order_delete'),
    path('instruction_delete/<pk>', InstructionDeleteView.as_view(), name='instruction_delete'),
    #Срок
    path('time_out/', time_out, name='time_out'),
    path('time_out_for_admin/', time_out_for_admin, name='time_out_for_admin'),
    #Ознакомление
    path('add_f_inst/', add_familiarization_instruction, name='add_f_inst'),
    path('ref_inst/<pk>', InstructionReferenceList.as_view(), name='ref_inst'),
    #PDF
    path('pdf/', pdf, name='pdf'),
    path('pdf_form/', add_pdf, name='pdf_form'),
    #Exel
    # path(r'^export/xls/$/<int:employee_id>', export_users_xls, name='export_users_xls'),
    path('export/xls/<int:employee_id>', export_users_xls, name='export_users_xls'),
    #Поиск
    path('search/', search, name='search'),
]