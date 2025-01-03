from misc.validator import DateValidator
from services.patient_mgr import PatientManager
from views.main import render_view

def run_program():
    patient_mgr = PatientManager()
    validator = DateValidator()
    main = render_view(patient_mgr, validator)
    main.run_program()