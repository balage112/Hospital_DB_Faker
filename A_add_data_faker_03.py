from A_create_db_01 import cr_seassion
from A_models_02 import *
from faker import Faker
from tqdm import tqdm

faker = Faker(locale="cz_CZ")

try:
    s = cr_seassion()

    for i in range(100):
        contact = ContactsDoctors(contact_doctor_phone=faker.phone_number(), contact_doctor_email=faker.email())
        s.add_all([contact])
    s.commit()

    for i in range(100):
        contact_p = ContactsPatients(contact_patient_phone=faker.phone_number(), contact_patient_email=faker.email())
        s.add_all([contact_p])
    s.commit()

    with open("departments_list_csv.csv") as f:
        rows = f.readlines()
        for row in rows:
            dep = row.split(",")
            s.add(Departments(department=dep[0]))
        s.commit()

    for i in range(10):
        dep_h_doc = Departments_have_doctors(departments_id=faker.random_int(1,7),
                                             doctor_id=faker.random_int(1,100))
        s.add_all([dep_h_doc])
    s.commit()

    with open ("diag_3_csv.csv") as f:
        reader = f.readlines()
        for r in tqdm (reader[1:], desc="Loading data"):
            d = r.split(",")
            s.add(Diagnosis(code=d[0], name=d[1]))
        s.commit()


    for i in range(100):
        doctor = Doctor(first_name=faker.first_name(), last_name=faker.last_name(),
                        doctors_phone = faker.random_int(1,100),
                        doctors_email = faker.random_int(1,100))
        s.add_all([doctor])
    s.commit()

    with open("insurance_3.csv", encoding="utf-8") as f:
        rows = f.readlines()
        for row in rows:
            ins = row.split(",")
            s.add(Insurance(insurance_code=ins[0], insurance_name=ins[1], insurance_address=ins[2],insurance_ds=ins[3],
                  insurance_phone=ins[4], insurance_email=ins[5]))
        s.commit()


    for i in range(100):
        patient = Patient(first_name=faker.first_name(),
                          last_name=faker.last_name(),
                          diagnosis_id=faker.random_int(1,100),
                          patients_phone=faker.random_int(1,100),
                          patients_email=faker.random_int(1,100),
                          date_of_birth=faker.date(),
                          birth_code=faker.random_number(digits=10, fix_len=5),
                          gender=faker.random_element(elements=["M", "F"]),
                          insurance_id=faker.random_int(1, 7))

        s.add_all([patient])
    s.commit()

    for i in range(100):
        visit = Visits(doctor_id=faker.random_int(1,100),
                       patient_id=faker.random_int(1,100),
                       date_of_visit=faker.date(),
                       time_of_visit=faker.time())
        s.add_all([visit])
    s.commit()

except Error as err:
    print(err)

