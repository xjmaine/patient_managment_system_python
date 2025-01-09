from datetime import datetime
import re

class Patient:
    DATE_FORMAT_MSG = "%d-%m-%Y"
    DATE_REGEX_PATTERN_MSG = r'^\d{2}-\d{2}-\d{4}$'
    
    def __init__(self, first_name, last_name, date_of_birth, hometown, house_number, phone_number):
        """
        Initialize a new Patient object with the provided details.

        Parameters:
        first_name (str): The first name of the patient.
        last_name (str): The last name of the patient.
        date_of_birth (str): The date of birth of the patient in the format 'dd-mm-yyyy'.
        hometown (str): The hometown of the patient.
        house_number (str): The house number of the patient.
        phone_number (str): The phone number of the patient.

        Returns:
        None
        """
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.hometown = hometown
        self.house_number = house_number
        self.age = self.calculate_age()




    def calculate_age(self):
        """
        Calculate the age of the patient based on their date of birth.

        Parameters:
        self (Patient): The instance of the Patient class.

        Returns:
        int: The age of the patient.
        """
        birth_date = datetime.strptime(self.date_of_birth, self.DATE_FORMAT_MSG)
        today = datetime.now()
        age = today.year - birth_date.year
        if (today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day)):
            age -= 1
        return age


    def patient_record_dict(self):
        """
        Generate a dictionary representation of the patient's details.

        Parameters:
        self (Patient): The instance of the Patient class.

        Returns:
        dict: A dictionary containing the patient's details. The dictionary keys are:
              'id': The patient's unique identifier.
              'first_name': The patient's first name.
              'last_name': The patient's last name.
              'date_of_birth': The patient's date of birth in 'dd-mm-yyyy' format.
              'phone_number': The patient's phone number.
              'hometown': The patient's hometown.
              'house_number': The patient's house number.
              'age': The patient's age calculated based on their date of birth.
        """
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'date_of_birth': self.date_of_birth,
            'phone_number': self.phone_number,
            'hometown': self.hometown,
            'house_number': self.house_number,
            'age': self.age
        }


class PatientMgr:
    DATE_OF_BIRTH_MSG = 'date_of_birth'
    def __init__(self):
        self.patients = []
        self.next_id = 1

    def add_patient(self, patient):
        """
        Add a new patient to the patient management system.

        Parameters:
        patient (Patient): An instance of the Patient class representing the patient to be added.

        Returns:
        int: The unique identifier assigned to the newly added patient.
        """
        patient.id = self.next_id
        self.patients.append(patient)
        self.next_id += 1
        return patient.id


    def get_all_patients(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return [patient.patient_record_dict() for patient in self.patients]

    def get_patient_by_id(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def update_patient(self, patient_id, **kwargs):
        patient = self.get_patient_by_id(patient_id)
        if not patient:
            return False

        for key, value in kwargs.items():
            if hasattr(patient, key):
                setattr(patient, key, value)
                if key == PatientMgr.DATE_OF_BIRTH_MSG:
                    patient.age = patient.calculate_age()
        return True

    def delete_patient(self, patient_id):
        patient = self.get_patient_by_id(patient_id)
        if patient:
            self.patients.remove(patient)
            return True
        return False

class Validator:
    DATE_REGEX_PATTERN_MSG = r'^\d{2}-\d{2}-\d{4}$'
    
    def validate_date_format(self, date_str: str):
        if not re.match(self.DATE_REGEX_PATTERN_MSG, date_str):
            raise ValueError("Invalid date format")

        day, month, year = map(int, date_str.split('-'))

        if month < 1 or month > 12:
            raise ValueError("Month must be between 01 and 12")

        if month == 2:
            if day > 29:
                raise ValueError("February cannot have more than 29 days")
            if day == 29:
                if not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    raise ValueError("February can only have 29 days in a leap year")

        try:
            datetime.strptime(date_str, Patient.DATE_FORMAT_MSG)
        except ValueError:
            raise ValueError("Invalid date")

        return True
    
    def validate_phone_number(self, phone_number: str) -> bool:
        """_summary_

        Args:
            phone_number (str): _description_

        Returns:
            bool: _description_
        """
        phone_number_pattern = re.compile(r"^\d{3}-\d{3}-\d{4}$")
        return bool(phone_number_pattern.fullmatch(phone_number))

def display_menu():
    print("\nPatient Management System")
    print("1. Add New Patient")
    print("2. Get All Patients")
    print("3. Search Patient by ID")
    print("4. Update Patient by ID")
    print("5. Delete Patient by ID")
    print("6. Exit")

def main_view():
    mgr = PatientMgr()
    validator = Validator()

    while True:
        display_menu()
        choice = input("Make your choice (1-6): ")

        if choice == '1':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            date_of_birth = input("Date of Birth (dd-mm-yyyy): ")
            try:
                validator.validate_date_format(date_of_birth)
            except ValueError as e:
                print(e)
                continue
            hometown = input("Hometown: ")
            house_number = input("House Number: ")
            
            while True:
                phone_number = input("Phone Number (xxx-xxx-xxxx): ")
                if validator.validate_phone_number(phone_number):
                    break
                else:
                    print("Invalid phone number format. Please use xxx-xxx-xxxx.")
            patient = Patient(first_name, last_name, date_of_birth, hometown, house_number, phone_number)
            patient_id = mgr.add_patient(patient)
            print(f"Patient added successfully with ID: {patient_id}")

        elif choice == '2':
            patients = mgr.get_all_patients()
            if not patients:
                print("No patients found.")
            else:
                for patient in patients:
                    print(patient)

        elif choice == '3':
            try:
                patient_id = int(input("Enter patient ID: "))
            except ValueError:
                print("Invalid ID format. Please enter a number.")
                continue
            patient = mgr.get_patient_by_id(patient_id)
            if not patient:
                print("Patient not found.")
            else:
                print(patient.patient_record_dict())

        elif choice == '4':
            try:
                patient_id = int(input("Enter patient ID to update: "))
            except ValueError:
                print("Invalid ID format. Please enter a number.")
                continue
            patient = mgr.get_patient_by_id(patient_id)
            if not patient:
                print("Patient not found.")
                continue
            
            print("Enter new values (or press enter to skip):")
            first_name = input(f"First Name [{patient.first_name}]: ")
            last_name = input(f"Last Name [{patient.last_name}]: ")
            date_of_birth = input(f"Date of Birth (dd-mm-yyyy) [{patient.date_of_birth}]: ")
            hometown = input(f"Hometown [{patient.hometown}]: ")
            house_number = input(f"House Number [{patient.house_number}]: ")
            phone_number = input(f'Phone Number [{patient.phone_number}]: ')

            updates = {}
            if first_name:
                updates['first_name'] = first_name
            if last_name:
                updates['last_name'] = last_name
            if date_of_birth:
                try:
                    validator.validate_date_format(date_of_birth)
                    updates['date_of_birth'] = date_of_birth
                except ValueError as e:
                    print(e)
                    continue
            if hometown:
                updates['hometown'] = hometown
            if house_number:
                updates['house_number'] = house_number

            if mgr.update_patient(patient_id, **updates):
                print("Patient updated successfully.")
            else:
                print("Update failed.")

        elif choice == '5':
            try:
                patient_id = int(input("Enter patient ID to delete: "))
            except ValueError:
                print("Invalid ID format. Please enter a number.")
                continue
            if mgr.delete_patient(patient_id):
                print("Patient deleted successfully.")
            else:
                print("Patient not found.")

        elif choice == '6':
            print("Thank you for using the Patient Management System!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_view()