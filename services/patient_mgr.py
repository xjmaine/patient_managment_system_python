class PatientManager:
    def __init__(self):
            self.patients = []
            self.next_id = 1

    def add_patient(self, patient):
        patient.id = self.next_id
        self.patients.append(patient)
        self.next_id += 1
        return patient.id


    def get_all_patients(self):
        return [
            patient.patient_record_dict() for patient in self.patients
            ]



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
                if key == 'date_of_birth':
                    patient.age = patient.calculate_age()
        return True

    def delete_patient(self, patient_id):
        patient = self.get_patient_by_id(patient_id)
        if patient:
            self.patients.remove(patient)
            return True
        return False