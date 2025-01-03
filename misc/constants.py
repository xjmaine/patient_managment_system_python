class ReusableString:
    # menu items
    MENU_TITLE_MSG = "\n Patient Management System"
    MENU_ADD_MSG = "1. Add New Patient"
    MENU_GET_ALL_MSG = "2. Get All Patient"
    MENU_SEARCH_MSG = "3. Search Patient by ID"
    MENU_UPDATE_MSG = "4. Update Patient by ID"
    MENU_DELETE_MSG = "5. Delete Patient by ID"
    MENU_EXIT_MSG = "6. Exit"
    MENU_CHOICE_MSG = "Make your choice (1-6): "
    
    #input prompts
    PROMPT_FIRST_NAME_MSG = "First Name: "
    PROMPT_LAST_NAME_MSG = "Last Name: "
    PROMPT_DOB_MSG = "Date of Birth (dd-mm-yyyy): "
    PROMPT_HOMETOWN_MSG = "Enter hometown: "
    PROMPT_HOUSE_NUMBER_MSG = "Enter house number: "
    PROMPT_PATIENT_ID_MSG = "Enter patient ID: "
    PROMPT_PATIENT_ID_UPDATE_MSG = "Enter patient ID to update: "
    PROMPT_PATIENT_ID_DELETE_MSG = "Enter patient ID to delete: "
    PROMPT_NEW_VALUE_MSG = "Enter new values (or press enter to skip):"
    PROMPT_NEW_FIELD_MSG = "New {}: "
    
    # Success messages
    SUCCESS_PATIENT_ADDED_MSG = "======>Patient added successfully with ID: {} <================================"
    SUCCESS_PATIENT_UPDATED_MSG = "Patient updated successfully."
    SUCCESS_PATIENT_DELETED_MSG = "Patient deleted successfully."
    SUCCESS_EXIT_MSG = "Thank you for using the Patient Management System!"

    # Error messages
    ERROR_INVALID_CHOICE_MSG = "Invalid choice. Please try again."
    ERROR_NO_PATIENTS_MSG = "No patients found."
    ERROR_PATIENT_NOT_FOUND_MSG = "Patient not found."
    ERROR_UPDATE_FAILED_MSG = "Update failed."
    ERROR_INVALID_DATE_MSG = "Date must be in dd-mm-yyyy format"
    ERROR_INVALID_MONTH_MSG = "Month must be between 01 and 12"
    ERROR_FEB_MAX_DAYS_MSG = "February cannot have more than 29 days"
    ERROR_FEB_LEAP_YEAR_MSG = "February can only have 29 days in a leap year"
    ERROR_INVALID_DATE_FORMAT_MSG = "Invalid date"
    ERROR_IN_INPUT_MSG = "Error in input: {}"

    # Field names
    FIELD_ID_MSG = 'id'
    FIELD_FIRST_NAME_MSG = 'first_name'
    FIELD_LAST_NAME_MSG = 'last_name'
    FIELD_DOB_MSG = 'date_of_birth'
    FIELD_AGE_MSG = 'age'
    FIELD_HOMETOWN_MSG = 'hometown'
    FIELD_HOUSE_NUMBER_MSG = 'house_number'

    # Date format
    DATE_FORMAT_MSG = "%d-%m-%Y"
    DATE_REGEX_PATTERN_MSG = r'^\d{2}-\d{2}-\d{4}$'
    