"""
TODO: Implement the Patient class.
Please import and use the config and db config variables.

The attributes for this class should be the same as the columns in the PATIENTS_TABLE.

The Object Arguments should only be name , gender and age.
Rest of the attributes should be set within the class.

-> for id use uuid4 to generate a unique id for each patient.
-> for checkin and checkout use the current date and time.

There should be a method to update the patient's room and ward. validation should be used.(config is given)

Validation should be done for all of the variables in config and db_config.

There should be a method to commit that patient to the database using the api_controller.
"""

import uuid
from datetime import datetime
from config import GENDERS, ROOM_NUMBERS, WARD_NUMBERS
from patient_db_config import PATIENTS_TABLE
from patient_db import PatientDB


class Patient:
    def __init__(self, name, gender, age):
        self.id = None
        self.name = name
        if gender in GENDERS:
            self.gender = gender
        else:
            raise ValueError("Invalid gender")
        self.age = age
        self.checkin = datetime.now().isoformat()
        self.checkout = "None"
        self.ward = None
        self.room = None

    def set_room(self, room):
        for key,value in ROOM_NUMBERS.items():
            if str(room) in value:
                self.room = room
                return
    
        raise ValueError("Invalid room or ward")
        
        
    def set_ward(self, ward):
        if ward in WARD_NUMBERS:
            self.ward = ward
        else:
            raise ValueError("Invalid room or ward")

    def get_id(self):
        return str(self.id)
    
    def get_name(self):
        return self.name

    def get_room(self):
        return self.room
    
    def get_ward(self):
        return self.ward

    def commit(self):
        try:
            self.id=str(uuid.uuid4())
            PatientDB().insert_patient({
                "patient_id":self.id,
                "patient_name":self.name,
                "patient_age":self.age,
                "patient_gender":self.gender,
                "patient_checkin":self.checkin,
                "patient_checkout":self.checkout,
                "patient_ward":self.ward,
                "patient_room":self.room
            }
            )

            return "Patient added to database successfully."
        except Exception as e:
            return f"Failed to add patient to database: {str(e)}"



