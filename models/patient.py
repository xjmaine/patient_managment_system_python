from datetime import datetime
from misc.constants import ReusableString

class Patient:
    def __init__(self, first_name, last_name, date_of_birth, hometown, house_number):
        self.id = None
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.hometown = hometown
        self.house_number = house_number
        self.age = self.calculate_age()
        
    
    def calculate_age(self):
        birth_date = datetime.strptime(self.date_of_birth, ReusableString.DATE_FORMAT_MSG)
        today = datetime.now()
        age = today.year - birth_date.year 
        if (today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day)):
            age -= 1
        return age
    
    
    def patient_record_dict(object):
        return{
            ReusableString.FIELD_ID_MSG: object.id,
            ReusableString.FIELD_FIRST_NAME_MSG: object.first_name,
            ReusableString.FIELD_LAST_NAME_MSG: object.last_name,
            ReusableString.FIELD_DOB_MSG: object.date_of_birth,
            ReusableString.FIELD_HOMETOWN_MSG: object.hometown,
            ReusableString.FIELD_HOUSE_NUMBER_MSG: object.house_number,
            ReusableString.FIELD_AGE_MSG: object.age
            
        }