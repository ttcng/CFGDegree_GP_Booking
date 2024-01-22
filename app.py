from flask import Flask, jsonify, request
from db_utils import get_all_booking_availability, add_a_booking, get_available_doctors, getPatientID, delete_booking, add_patient

app = Flask(__name__)

# Information about availability
# e.g. using http://127.0.0.1:5001/availability/2021-07-01
@app.route('/availability/<date>')
def get_bookings(date):
    res = get_all_booking_availability(date)
    return jsonify(res)

# Endpoint for patient ID from DOB and surname
@app.route('/patientID/<patient_DOB>/<patient_surname>')
def get_patient_ID_app(patient_DOB, patient_surname):
    res = getPatientID(patient_DOB, patient_surname)
    return res


# Endpoint for available doctors
@app.route('/availableDoctors/<date>/<time>')
def available_doctors(date, time):
    res = get_available_doctors(date,time)
    return jsonify(res)

# To add an appointment
@app.route('/booking', methods=['PUT'])
def book_appt():
    booking = request.get_json()
    add_a_booking(
        _date=booking['_date'],
        doctor=booking['doctor'],
        time=booking['time'],
        patient=booking['patient'],
    )

    return booking

# Cancel booking
@app.route('/cancel_booking', methods=['PUT'])
def cancel_appt():
    booking = request.get_json()

    delete_booking(
        booking_date=booking['booking_date'],
        time_slot_column_name=booking['time_slot_column_name'],
        patientID=booking['patientID'],
    )

    return booking

@app.route('/add_patient', methods=['POST'])
def new_patient():
    patient = request.get_json()
    print(patient)
    record = {
        'surname': patient['surname'],
        'firstname': patient['firstname'],
        'DOB': patient['DOB'],
        'gender': patient['gender'],
    }

    add_patient(record)

    return patient

if __name__ == '__main__':
    app.run(debug=True, port=5001)