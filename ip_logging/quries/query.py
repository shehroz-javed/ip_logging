from datetime import date, datetime, timedelta

from quries.models import Doctor, Nurse, Patient, Hospital, MedicalRecord

# task 1

# - Retrieve all patients admitted on a specific date.
query_date = date(2024, 7, 22)
patients = Patient.objects.filter(date_admitted__date=query_date)

# - Get the names of all doctors who have patients with a specific diagnosis.
diagnoses = "test"
doctors_name = (
    MedicalRecord.objects.prefetch_related("patient__doctor")
    .filter(diagnoses=diagnoses)
    .values("patient__doctor__name")
    .distinct()
)

# - Find all patients treated by a particular nurse.
nurse_name = "Jacob Horn"
nurse_patients = Patient.objects.select_related("nurse").filter(nurse__name=nurse_name)

# - Retrieve the contact number of the doctor for a given patient.
id = 33
doctor_contact_number = (
    Patient.objects.prefetch_related("doctor")
    .filter(id=id)
    .values("doctor__contact_number")
)

# - Get the total number of patients admitted to the hospital.


# - Find the patients who are not assigned to any nurse.
patients = Patient.objects.filter(nurse__isnull=True)

# - Retrieve the names of nurses who have patients with a specific prescription.
prescription = "test"
nurses_name = (
    MedicalRecord.objects.select_related("patient__nurse")
    .filter(prescription=prescription)
    .values("patient__nurse__name")
)

# - Get the average age of patients in the hospital.


# - Find the most recently admitted patient.
latest_patient = Patient.objects.latest("date_admitted")

# - Retrieve all doctors who have more than five patients.
from django.db.models import Count

doctors = (
    Doctor.objects.prefetch_related("doctors")
    .annotate(num_of_patient=Count("doctors"))
    .filter(num_of_patient__gt=5)
)

# - Find the patients who have been admitted for more than a week.
filter_date = datetime.now() - timedelta(weeks=1)
patients = Patient.objects.filter(date_admitted__lt=filter_date)

# - Get the number of patients assigned to each nurse.
nurse = Nurse.objects.prefetch_related("nurses").all()
for n in nurse:
    print(n.nurses.all())

# - Retrieve the names of patients who have a specific doctor.
id = 40
patients_name = (
    Patient.objects.prefetch_related("doctor").filter(doctor__id=id).values("name")
)

# - Find the doctors who specialize in a specific medical field.
specialization = "test"
doctors = Doctor.objects.filter(specialization=specialization)

# - Get the names of patients treated by a doctor with a specific specialization.
specialization = "test"
patients_name = (
    Patient.objects.prefetch_related("doctor")
    .filter(doctor__specialization=specialization)
    .values("name")
)

# - Find the nurses who have not been assigned any patients.
nurse = Nurse.objects.prefetch_related("nurses").filter(nurses__isnull=True)

# - Retrieve the latest medical record for a given patient.
id = 33
latest_mr = MedicalRecord.objects.filter(patient_id=id).last()

# - Get the names of patients with a specific diagnosis.
diagnoses = "test"
patients_name = (
    MedicalRecord.objects.select_related("patient")
    .filter(diagnoses=diagnoses)
    .values("patient__name")
)

# - Find the doctors who have patients of a certain age group.
doctors = (
    Doctor.objects.prefetch_related("doctors")
    .filter(doctors__age__gte=30, doctors__age__lte=35)
    .distinct()
)

# - Retrieve all patients with a specific prescription.
prescription = "test"
patients = (
    Patient.objects.prefetch_related("mr_patients")
    .filter(mr_patients__prescription=prescription)
    .distinct()
)

# - Find the nurses who have patients with a specific age.
nurse = Nurse.objects.prefetch_related("nurses").filter(nurses__age=20).distinct()

# - Get the total number of medical records in the system.
total_mr = MedicalRecord.objects.all().count()

# - Retrieve the names of patients treated by a nurse with a specific contact number.
contact_number = "12345"
patients = Patient.objects.filter(nurse__contact_number=contact_number).values("name")

# - Find the patients who are treated by more than one doctor.
patients = Patient.objects.annotate(num_of_doc=Count("doctor")).filter(num_of_doc__gt=1)

# - Get the names of doctors who have treated patients with a specific prescription.
prescription = "test"
doctors_name = (
    MedicalRecord.objects.prefetch_related("patient__doctor")
    .filter(prescription=prescription)
    .values("patient__doctor__name")
    .distinct()
)

# - Find the patients who have not been assigned to any doctor.
patients = Patient.objects.filter(doctor__isnull=True)

# - Retrieve the doctors who have patients admitted on a specific date.
query_date = date(2024, 7, 22)
doctors = (
    Doctor.objects.prefetch_related("doctors")
    .filter(doctors__date_admitted__date=query_date)
    .distinct()
)

# - Get the number of patients admitted each month.
from django.db.models.functions import ExtractMonth

number_of_patient = (
    Patient.objects.annotate(month=ExtractMonth("date_admitted"))
    .values("month")
    .annotate(count=Count("id"))
    .values("month", "count")
)

# - Find the patients with the highest age in the hospital.

# - Retrieve all nurses who have patients admitted on a specific date.
query_date = date(2024, 7, 22)
nurses = (
    Nurse.objects.prefetch_related("nurses")
    .filter(nurses__date_admitted__date=query_date)
    .distinct()
)

# - Find the doctors who have patients with a specific age.
doctor = Doctor.objects.prefetch_related("doctors").filter(doctors__age=20).distinct()

# - Get the number of patients treated by each doctor.
doctor = Doctor.objects.prefetch_related("doctors").all()
for d in doctor:
    print(d.doctors.all())

# - Retrieve the names of patients with a specific age.
patients = Patient.objects.filter(age=20).values_list("name", flat=True)

# - Find the nurses who have patients with a specific diagnosis.
diagnoses = "test"
nurses = (
    Nurse.objects.prefetch_related("nurses__mr_patients")
    .filter(nurses__mr_patients__diagnoses=diagnoses)
    .distinct()
)

# - Find the doctors who have not been assigned any patients.
doctor = Doctor.objects.prefetch_related("doctors").filter(doctors__isnull=True)

# - Retrieve the patients who have medical records with a specific prescription.
prescription = "test"
patients = (
    Patient.objects.prefetch_related("mr_patients")
    .filter(mr_patients__prescription=prescription)
    .distinct()
)

# - Get the average age of patients treated by each doctor.
from django.db.models import Avg

doctors = Doctor.objects.prefetch_related("doctors").annotate(
    avg_age=Avg("doctors__age")
)

# - Find the doctors who have patients with a specific prescription.
prescription = "test"
doctors = (
    Doctor.objects.prefetch_related("doctors__mr_patients")
    .filter(doctors__mr_patients__prescription=prescription)
    .distinct()
)

# - Retrieve the names of patients treated by a doctor with a specific contact number.
contact_number = "12345"
patients = (
    Patient.objects.prefetch_related("doctor")
    .filter(doctor__contact_number=contact_number)
    .values("name")
)

# - Find the nurses who have patients with a specific prescription.
prescription = "test"
nurses = (
    Nurse.objects.prefetch_related("nurses__mr_patients")
    .filter(nurses__mr_patients__prescription=prescription)
    .distinct()
)

# - Get the total number of patients treated by nurses in a specific specialization.
None

# - Retrieve the patients who have not been assigned to any nurse.
patients = Patient.objects.filter(nurse__isnull=True)

# - Find the doctors who have patients admitted for more than a week.
filter_date = datetime.now() - timedelta(weeks=1)
doctors = Doctor.objects.prefetch_related("doctors").filter(
    doctors__date_admitted__lt=filter_date
)

# - Get the names of patients with a specific diagnosis treated by a specific doctor.
diagnosis = "test"
doctor = Doctor.objects.filter(id=37).first()
patients = (
    Patient.objects.prefetch_related("mr_patients")
    .filter(mr_patients__diagnoses=diagnosis)
    .distinct()
)
patients_names = patients.filter(doctor=doctor).values("name")

# - Find the nurses who have patients with a specific age group.
nurses = (
    Nurse.objects.prefetch_related("nurses")
    .filter(nurses__age__gte=30, nurses__age__lte=35)
    .distinct()
)

# - Retrieve the doctors who have patients with a specific diagnosis and age group.
diagnosis = "test"
doctor = (
    Doctor.objects.prefetch_related("doctors", "doctors__mr_patients")
    .filter(
        doctors__age__gte=30,
        doctors__age__lte=35,
        doctors__mr_patients__diagnoses="test",
    )
    .distinct()
)

# - Get the number of patients treated by each nurse in a specific specialization.
None

# - Find the patients who have been treated by more than one nurse.


# - Retrieve the names of doctors who have patients with a specific diagnosis and age group.
diagnosis = "test"
doctor = (
    Doctor.objects.prefetch_related("doctors", "doctors__mr_patients")
    .filter(
        doctors__age__gte=30,
        doctors__age__lte=35,
        doctors__mr_patients__diagnoses="test",
    )
    .values("name")
    .distinct()
)


# task 2

# - Select all patients with their associated doctors and nurses.
# - Select all patients admitted after a specific date.
# - Count the total number of patients.
# - Count the total number of patients with a specific age.
# - Select all patients with their associated doctors and nurses prefetched.
# - Count the total number of doctors associated with each patient.
# - Sum the ages of all patients.
# - Select all patients along with the number of doctors associated with each.
# - Select all patients along with their medical records, if available.
# - Count the total number of nurses associated with each patient.
# - Select all patients with their associated nurses and the nurses' contact numbers.
# - Select all patients along with the total number of medical records for each.
# - Select all patients with their diagnoses and prescriptions, if available.
# - Count the total number of patients admitted in a specific year.
# - Select all patients along with their doctors' specializations.
# - Select all patients along with the count of medical records for each.
# - Select all doctors with the count of patients they are associated with.
# - Select all patients along with the count of nurses they are associated with.
# - Annotate the average age of patients.
# - Annotate the maximum age of patients.
# - Annotate the minimum age of patients.
# - Select all patients along with the earliest admission date.
# - Select all doctors with their associated patients prefetched.
# - Select all nurses with their associated patients prefetched.
# - Select all patients along with the count of distinct doctors they are associated with.
