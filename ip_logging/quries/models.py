from django.db import models

# 1. class Doctor: name(str) specialization(str) contact_number(str)
# 2. class Nurse: name(str) contact_number(str)
# 3. class Patient: name(str) age(int) doctor(ManyToManyField, related_name='doctors') nurse(ForeignKey, on_delete=models.CASCADE, related_name='nurses') date_admitted(DateTimeField, auto_now_add=True)
# 4. class Hospital: patient(ForeignKey, on_delete=models.CASCADE, related_name='patients') doctor(ManyToManyField) nurse(ForeignKey, on_delete=models.CASCADE)
# 5. class MedicalRecord: patient(ForeignKey, on_delete=models.CASCADE, related_name='patients') diagnoses(TextField) prescription(TextField)


class Doctor(models.Model):

    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Nurse(models.Model):

    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):

    name = models.CharField(max_length=255)
    age = models.IntegerField()
    doctor = models.ManyToManyField(Doctor, related_name="doctors")
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE, related_name="nurses")
    date_admitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="patients"
    )
    doctor = models.ManyToManyField(Doctor)
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.patient.name} - {self.nurse.name}"


class MedicalRecord(models.Model):

    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="mr_patients"
    )
    diagnoses = models.TextField()
    prescription = models.TextField()

    def __str__(self):
        return f"{self.patient.name} - Medical Record"
