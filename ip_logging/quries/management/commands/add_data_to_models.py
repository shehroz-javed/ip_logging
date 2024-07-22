import random
from faker import Faker

from django.core.management.base import BaseCommand

from quries.models import Doctor, Nurse, Patient, Hospital, MedicalRecord


class Command(BaseCommand):
    help = "Add data to the models"

    def handle(self, *args, **options):

        faker = Faker()

        doctors = []
        for i in range(10):
            doctor = Doctor.objects.create(
                name=faker.name(),
                specialization=faker.job(),
                contact_number=faker.phone_number(),
            )
            doctors.append(doctor)

        nurses = []
        for i in range(20):
            nurse = Nurse.objects.create(
                name=faker.name(),
                contact_number=faker.phone_number(),
            )
            nurses.append(nurse)

        patients = []
        for i in range(30):
            patient = Patient.objects.create(
                name=faker.name(),
                age=random.randint(1, 50),
                nurse=random.choice(nurses),
            )
            random_doctor = random.sample(doctors, random.randint(1, 3))
            patient.doctor.set(random_doctor)
            patients.append(patient)

        for i in range(5):
            hospital = Hospital.objects.create(
                patient=random.choice(patients),
                nurse=random.choice(nurses),
            )
            random_doctor = random.sample(doctors, random.randint(1, 3))
            hospital.doctor.set(random_doctor)

        for patient in patients:
            medical_record = MedicalRecord.objects.create(
                patient=patient,
                diagnoses=faker.text(max_nb_chars=200),
                prescription=faker.text(max_nb_chars=200),
            )

        self.stdout.write(self.style.SUCCESS("Data added successfully"))
