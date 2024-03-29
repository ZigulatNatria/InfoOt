from django.contrib import admin
from .models import Employee, Medicine, Psycho, Passport, Education, Certificate, MedicineParagraph, Subdivision, \
    Profession, Sawc, Order, Instruction, FamiliarizationInstruction, MedicineParagraphList, CertificateNameList, \
    SafeSystems, Department

# Register your models here.
admin.site.register(Employee)
admin.site.register(Medicine)
admin.site.register(Psycho)
admin.site.register(Passport)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(MedicineParagraph)
admin.site.register(Subdivision)
admin.site.register(Department)
admin.site.register(Profession)
admin.site.register(Sawc)
admin.site.register(Order)
admin.site.register(Instruction)
admin.site.register(FamiliarizationInstruction)
admin.site.register(MedicineParagraphList)
admin.site.register(CertificateNameList)
admin.site.register(SafeSystems)
