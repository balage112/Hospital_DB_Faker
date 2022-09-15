from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy import Column, Integer, String, Date, DateTime, Time, ForeignKey, PrimaryKeyConstraint,null
from mysql.connector import Error
from A_create_db_01 import cr_engine

Base = declarative_base()

try:
    e = cr_engine()
    if not database_exists(e.url):
        create_database(e.url)

    class ContactsDoctors(Base):
        __tablename__ = "contacts_doctors"
        id = Column(Integer, primary_key=True, autoincrement=True)
        contact_doctor_phone = Column(String(100))
        contact_doctor_email = Column(String(100))

    class ContactsPatients(Base):
        __tablename__ = "contacts_patients"
        id = Column(Integer, primary_key=True, autoincrement=True)
        contact_patient_phone = Column(String(100))
        contact_patient_email = Column(String(100))

    class Departments(Base):
        __tablename__ = "departments"
        id = Column(Integer,autoincrement=True, primary_key=True)
        department = Column(String(45))

        def __str__(self):
            return f"Department: {self.department}"

    class Departments_have_doctors(Base):
        __tablename__ = "departments_have_doctor"
        id = Column(Integer, autoincrement=True, primary_key=True)
        departments_id = Column(Integer)
        doctor_id = Column(Integer)

    class Diagnosis(Base):
        __tablename__ = "diagnosis"
        id = Column(Integer, autoincrement=True, primary_key=True)
        name = Column(String(256))
        code = Column(String(20))

        def __str__(self):
            return f"Diagnosis: {self.name}"

    class Doctor(Base):
        __tablename__ = "doctors"
        id = Column(Integer, autoincrement=True, primary_key=True)
        first_name = Column(String(40))
        last_name = Column(String(40))
        doctors_phone = Column(Integer)
        doctors_email = Column(Integer)

        def __str__(self):
            return f"Doctors: {self.first_name}, {self.last_name}"


    class Insurance(Base):
        __tablename__ = "insurance"
        id = Column(Integer, primary_key=True, autoincrement=True)
        insurance_code = Column(String(10))
        insurance_name = Column(String(100))
        insurance_address = Column(String(100))
        insurance_ds = Column(String(40))
        insurance_phone = Column(String(100))
        insurance_email = Column(String(100))

        def __str__(self):
            return f"Insurance: {self.insurance_code}," \
                   f" {self.insurance_name}"


    class Patient(Base):
        __tablename__ = "patients"
        id = Column(Integer, primary_key=True, autoincrement=True)
        first_name = Column(String(40))
        last_name = Column(String(40))
        diagnosis_id = Column(Integer)
        patients_phone = Column(Integer)
        patients_email = Column(Integer)
        date_of_birth = Column(String(10))
        birth_code = Column(String(10))
        gender = Column(String(2))
        insurance_id = Column(Integer)

        def __str__(self):
            return f"Patients: {self.first_name}, {self.last_name}, {self.date_of_birth}, {self.birth_code}," \
                   f"{self.gender}, {self.insurance_id}"


    class Visits(Base):
        __tablename__ = "visits"
        id = Column(Integer, primary_key=True, autoincrement=True)
        doctor_id = Column(Integer)
        patient_id = Column(Integer)
        date_of_visit = Column(Date)
        time_of_visit = Column(Time)
        commentary = Column(String(1000))

        def __str__(self):
            return f"Visits: {self.doctor_id}, {self.patient_id}, {self.date_of_visit}, {self.time_of_visit}, " \
                   f"{self.commentary}"

    Base.metadata.create_all(e)

except Error as e:
    print(e)

