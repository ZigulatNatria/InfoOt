from django.contrib import admin
from .models import Employee, Medicine, Psycho, Passport, Education, Certificate, MedicineParagraph

# Register your models here.
admin.site.register(Employee)
admin.site.register(Medicine)
admin.site.register(Psycho)
admin.site.register(Passport)
admin.site.register(Education)
admin.site.register(Certificate)
admin.site.register(MedicineParagraph)
