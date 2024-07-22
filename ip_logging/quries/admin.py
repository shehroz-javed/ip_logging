from django.contrib import admin
from quries.models import Doctor, Nurse, Patient, Hospital, MedicalRecord


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "specialization", "contact_number"]


@admin.register(Nurse)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "contact_number"]


@admin.register(Patient)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["name", "age", "nurse", "date_admitted"]


@admin.register(MedicalRecord)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["diagnoses", "prescription"]


admin.site.register(Hospital),
