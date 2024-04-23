"""Patient API Controller"""

from flask import Flask, jsonify, request
from patient_db import PatientDB


class PatientAPIController:
    def __init__(self):
        self.app = Flask(__name__)
        self.patient_db = PatientDB()
        self.setup_routes()
        self.run()

    def setup_routes(self):
        """
        Sets up the routes for the API endpoints.
        """
        self.app.route("/patients", methods=["GET"])(self.get_patients)
        self.app.route("/patients/<patient_id>", methods=["GET"])(self.get_patient)
        self.app.route("/patients", methods=["POST"])(self.create_patient)
        self.app.route("/patient/<patient_id>", methods=["PUT"])(self.update_patient)
        self.app.route("/patient/<patient_id>", methods=["DELETE"])(self.delete_patient)


    """
    TODO:
    Implement the following methods,
    use the self.patient_db object to interact with the database.

    Every method in this class should return a JSON response with status code
    Status code should be 200 if the operation was successful,
    Status code should be 400 if there was a client error,
    """

    def create_patient(self):
        data = request.json
    # Here you should include data validation
        if 'patient_name' in data and 'patient_age' in data:  # Example validation
            result = self.patient_db.insert_patient(data)
            return jsonify(result), 200
        else:
            return jsonify({"error": "Missing data"}), 400

    def get_patients(self):
        patients = self.patient_db.select_all_patients()
        return jsonify(patients), 200

    def get_patient(self, patient_id):
        patient = self.patient_db.select_patient(patient_id)
        if patient:
            return jsonify(patient), 200
        else:
            return jsonify({"error": "Patient not found"}), 404
        
    def update_patient(self, patient_id):
        data = request.get_json()
        if self.patient_db.update_patient(patient_id, data):
            return jsonify({"success": "Patient updated"}), 200
        else:
            return jsonify({"error": "Update failed"}), 400

    def delete_patient(self, patient_id):
        if self.patient_db.delete_patient(patient_id):
            return jsonify({"success": "Patient deleted"}), 200
        else:
            return jsonify({"error": "Delete failed"}), 400

    def run(self):
        self.app.run(debug=True) 


PatientAPIController()
