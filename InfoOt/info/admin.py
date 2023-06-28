from django.contrib import admin
from .models import Employee, Medicine, Psycho, Passport, Education, Certificate, MedicineParagraph, Subdivision, \
    Profession, Sawc

# Register your models here.
admin.site.register(Employee)
admin.site.register(Medicine)
admin.site.register(Psycho)
admin.site.register(Passport)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(MedicineParagraph)
admin.site.register(Subdivision)
admin.site.register(Profession)
admin.site.register(Sawc)
