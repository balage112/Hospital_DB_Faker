from A_models_02 import *
from A_create_db_01 import cr_seassion
s = cr_seassion()
from sqlalchemy import or_, not_, and_,union,union_all,intersect,except_, join, outerjoin


print("_" * 100)
print()

op = "Welcome to hospital central system (HCS)."
print(op)

print("_" * 100)
print()

opening_phrase = "\n1: Show doctors database. \n2: Show patients database." \
                 " \n3: Search doctor.  \n4: Search patient:    " \
                 "\n5: Show diagnose.    \n6: Add commentary.    "\
                    "\n7: Show commentary. "\

def empty_row():
    print()

def show_doctors_db():
    print("Doctors database.")
    doctors = s.query(Doctor).all()
    if doctors:
        for d in doctors:
            print(d)



def show_patients_db():
    patients = s.query(Patient.first_name, Patient.last_name)
    if patients:
        for p, l in patients:
            print(p,l)


def find_doctor():
    f = input("Type  FIRST NAME of the doctor:      ")
    l = input("Type LAST NAME of the doctor:     ")
    empty_row()
    find = s.query(Doctor.first_name, Doctor.last_name).filter(Doctor.first_name == f).filter(and_(Doctor.last_name == l))
    if find:
        for f,l in find:
            print(f"Doctor: {f} {l} is working in hospital.")
            break
        else:
            print(f"{f} {l} is not working in our hospital.")


def search_patients():
    f = input("Type FIRST name of the patient:  ")
    l = input("Type LAST name of the patient:   ")
    empty_row()
    find = s.query(Patient.first_name, Patient.last_name).filter(Patient.first_name == f).filter(and_(
        Patient.last_name == l))
    if find:
        for f, l in find:
            print(f"Patient {f} {l} is in our hospital in ")
            break
        else:
            print(f"Patient {f} {l} is not in our hospital")


def show_diagnose():
    f = input("Type FIRST name of the patient:  ")
    l = input("Type LAST name of the patient:   ")
    empty_row()
    find = s.query(Patient.first_name, Patient.last_name).filter(Patient.first_name == f).filter(and_(
        Patient.last_name == l))
    diag = s.query(Diagnosis.name).filter(Patient.first_name == f).filter(and_(Patient.last_name == l))
    if find and diag:
        for d in diag:
            print(f"Patient {f} {l} has diagnose: {d}")
            break

def visit_commentary():
    f = input("Type FIRST name of the patient:  ")
    l= input("Type LAST name of the patient:   ")
    empty_row()
    find = s.query(Patient.first_name, Patient.last_name).filter(Patient.first_name == f).filter(and_(
        Patient.last_name == l))
    comment = s.query(Visits.commentary).filter(Patient.first_name == f).filter(and_(Patient.last_name == l))
    if find and comment:
        for c in comment:
            print(f"Patient {f} {l} has commentary: {c}")
            break
    add = input("Do you want to add commentary? (y/n)   ")
    if add == "y":
        c = input("Type commentary:   ")
        s.add(Visits(commentary=c))
        s.commit()
        print("Commentary added.")

# TODO nezobrazuje se komentar nutno upravit query, aby se komentar zobrazil - nutno zadat id pacienta a ne jeho jmeno a prijmeni
# TODO a zadat id doktora a ne jeho jmeno a prijmeni
# TODO přidat mazání komentářů
def show_commentary():
    f = input("Type FIRST name of the patient:  ")
    l = input("Type LAST name of the patient:   ")
    empty_row()
    find = s.query(Patient.first_name, Patient.last_name).filter(Patient.first_name == f).filter(and_(
        Patient.last_name == l))
    comment = s.query(Visits.commentary).filter(Patient.first_name == f).filter(and_(Patient.last_name == l))
    if find and comment:
        for c in comment:
            print(f"Patient {f} {l} has commentary: {c}")
            break

app_functions = {
    "1": show_doctors_db,
    "2": show_patients_db,
    "3": find_doctor,
    "4": search_patients,
    "5": show_diagnose,
    "6": visit_commentary,
    "7": show_commentary
    }