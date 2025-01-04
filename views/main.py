from misc.constants import ReusableString
from models.patient import Patient
from misc.validator import DateValidator

class render_view(object):
    def __init__(object, patient_mgr, validator):
        object.patient_mgr = patient_mgr
        object.validator = validator
        
    
    def display_menu(args):
        print(ReusableString.MENU_TITLE_MSG)
        print(ReusableString.MENU_ADD_MSG)
        print(ReusableString.MENU_GET_ALL_MSG)
        print(ReusableString.MENU_SEARCH_MSG)
        print(ReusableString.MENU_UPDATE_MSG)
        print(ReusableString.MENU_DELETE_MSG)
        print(ReusableString.MENU_EXIT_MSG)
    
    def get_patient_input(self):
        try:
            first_name = input(ReusableString.PROMPT_FIRST_NAME_MSG)
            last_name = input(ReusableString.PROMPT_LAST_NAME_MSG)
            while True:
                date_of_birth = input(ReusableString.PROMPT_DOB_MSG)
                try:
                    # self.validator.validate_date_format(date_of_birth)
                    DateValidator.validate_date_format(date_of_birth)
                    break
                except ValueError as e:
                    print(f"Error: {e}")
            
            hometown = input(ReusableString.PROMPT_HOMETOWN_MSG)
            house_number = input(ReusableString.PROMPT_HOUSE_NUMBER_MSG)
            
            return Patient(first_name, last_name, date_of_birth, hometown, house_number)
        except Exception as e:
            print(ReusableString.ERROR_IN_INPUT.format(e))
            return None
        
    def run_program(self):
        while True:
            self.display_menu()
            choice = input(ReusableString.MENU_CHOICE_MSG)
            
            if choice == '1':
                patient = self.get_patient_input()
                if patient:
                    patient_id = self.patient_mgr.add_patient(patient)
                    print(ReusableString.SUCCESS_PATIENT_ADDED_MSG.format(patient_id))
            
            elif choice == '2':
                patients = self.patient_mgr.get_all_patients()
                if patients:
                    for patient in patients:
                        print("\n".join(f"{k}: {v}" for k, v in patient.items()))
                        print("-" * 30)
                else:
                    print(ReusableString.ERROR_NO_PATIENTS_MSG)
            
            elif choice == '3':
                patient_id = int(input(ReusableString.PROMPT_PATIENT_ID_MSG))
                patient = self.patient_mgr.get_patient_by_id(patient_id)
                if patient:
                    print("\n".join(f"{k}: {v}" for k, v in patient.patient_record_dict().items()))
                else:
                    print(ReusableString.ERROR_PATIENT_NOT_FOUND_MSG)
            
            elif choice == '4':
                patient_id = int(input(ReusableString.PROMPT_PATIENT_ID_UPDATE_MSG))
                patient = self.patient_mgr.get_patient_by_id(patient_id)
                if patient:
                    print(ReusableString.PROMPT_NEW_VALUE_MSG)
                    updates = {}
                    for field in [ReusableString.FIELD_FIRST_NAME_MSG, ReusableString.FIELD_LAST_NAME_MSG, 
                                ReusableString.FIELD_DOB_MSG, ReusableString.FIELD_HOMETOWN_MSG, 
                                ReusableString.FIELD_HOUSE_NUMBER_MSG]:
                        value = input(ReusableString.PROMPT_NEW_FIELD_MSG.format(field))
                        if value:
                            if field == ReusableString.FIELD_DOB_MSG:
                                try:
                                    DateValidator.validate_date_format(value)
                                    updates[field] = value
                                except ValueError as e:
                                    print(f"Invalid date format: {e}")
                                    continue
                            else:
                                updates[field] = value
                    
                    if self.patient_mgr.update_patient(patient_id, **updates):
                        print(ReusableString.SUCCESS_PATIENT_UPDATED_MSG)
                    else:
                        print(ReusableString.ERROR_UPDATE_FAILED_MSG)
                        print(ReusableString.ERROR_UPDATE_FAILED_MSG)
                else:
                    print(ReusableString.ERROR_PATIENT_NOT_FOUND)
            
            elif choice == '5':
                patient_id = int(input(ReusableString.PROMPT_PATIENT_ID_DELETE_MSG))
                if self.patient_mgr.delete_patient(patient_id):
                    print(ReusableString.SUCCESS_PATIENT_DELETED_MSG)
                else:
                    print(ReusableString.ERROR_PATIENT_NOT_FOUND_MSG)
            
            elif choice == '6':
                print(ReusableString.SUCCESS_EXIT_MSG)
                break
            
            else:
                print(ReusableString.ERROR_INVALID_CHOICE_MSG)