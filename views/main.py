from misc.constants import Constants
from models.patient import Patient

class render_view(object):
    def __init__(object, patient_mgr, validator):
        object.patient_mgr = patient_mgr
        object.validator = validator
        
    
    def display_menu(args):
        print(Constants.MENU_TITLE_MSG)
        print(Constants.MENU_ADD_MSG)
        print(Constants.MENU_GET_ALL_MSG)
        print(Constants.MENU_SEARCH_MSG)
        print(Constants.MENU_UPDATE_MSG)
        print(Constants.MENU_DELETE_MSG)
        print(Constants.MENU_EXIT_MSG)
    
    def get_patient_input(self):
        try:
            first_name = input(Constants.PROMPT_FIRST_NAME_MSG)
            last_name = input(Constants.PROMPT_LAST_NAME_MSG)
            while True:
                date_of_birth = input(Constants.PROMPT_DOB_MSG)
                try:
                    self.validator.validate_date_format(date_of_birth)
                    break
                except ValueError as e:
                    print(f"Error: {e}")
            
            hometown = input(Constants.PROMPT_HOMETOWN_MSG)
            house_number = input(Constants.PROMPT_HOUSE_NUMBER_MSG)
            
            return Patient(first_name, last_name, date_of_birth, hometown, house_number)
        except Exception as e:
            print(Constants.ERROR_IN_INPUT.format(e))
            return None