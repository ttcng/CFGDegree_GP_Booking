import mysql.connector
from config import USERNAME, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USERNAME,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def _map_values(availability):
    mapped = []
    for item in availability:
        mapped.append(
            {
                'Doctor': item[0],
                '08:00-08:15': 'Not Available' if item[1] else 'Available',
                '08:15-08:30': 'Not Available' if item[2] else 'Available',
                '08:30-08:45': 'Not Available' if item[3] else 'Available',
                '08:45-09:00': 'Not Available' if item[4] else 'Available',
                '09:00-09:15': 'Not Available' if item[5] else 'Available',
                '09:15-09:30': 'Not Available' if item[6] else 'Available',
                '09:30-09:45': 'Not Available' if item[7] else 'Available',
                '09:45-10:00': 'Not Available' if item[8] else 'Available',
                '10:00-10:15': 'Not Available' if item[9] else 'Available',
                '10:15-10:30': 'Not Available' if item[10] else 'Available',
                '10:30-10:45': 'Not Available' if item[11] else 'Available',
                '10:45-11:00': 'Not Available' if item[12] else 'Available',
                '11:00-11:15': 'Not Available' if item[13] else 'Available',
                '11:15-11:30': 'Not Available' if item[14] else 'Available',
                '11:30-11:45': 'Not Available' if item[15] else 'Available',
                '11:45-12:00': 'Not Available' if item[16] else 'Available',
            }
        )
    return mapped


def get_all_booking_availability(_date):
    availability = []
    try:
        db_name = 'doctor'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            SELECT  Doctor, `08:00-08:15`, `08:15-08:30`, `08:30-08:45`, `08:45-09:00`, 
            `09:00-09:15`, `09:15-09:30`,
            `09:30-09:45`, `09:45-10:00`, `10:15-10:30`, `10:30-10:45`, `10:45-11:00`, 
            `11:00-11:15`, `11:15-11:30`,
            `11:15-11:30`, `11:30-11:45`, `11:30-11:45` ,`11:45-12:00`
            FROM doctor_availability_AM 
            WHERE bookingDate = '{}'
            """.format(_date)

        cur.execute(query)

        result = cur.fetchall()  # this is a list with db records where each record is a tuple
        availability = _map_values(result)

        for i in availability:
            print(i)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return availability


def add_patient(record):
    try:
        db_name = 'doctor'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """INSERT INTO patient_records (patient_surname, patient_firstname, patient_DOB, gender, date_joined, date_last_appt)
         VALUES ('{}', '{}', '{}', '{}', CURDATE(), NULL)""".format(
            record['surname'],
            record['firstname'],
            record['DOB'],
            record['gender'],
        )
        cur.execute(query)
        db_connection.commit()
        cur.close()

        print("Patient added successfully")

    except Exception as e:
        raise DbConnectionError(f"Failed to add patient: {e}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


record = {
    'Patient_id': 11,
    'surname': 'Hayes',
    'firstname': 'Matt',
    'DOB': 19960118,
    'gender': 'male',
    'joined_date': 20041018,
    'last_appt_date': 20220526

}


# adding a booking
def add_a_booking(_date, doctor, time, patient):
    try:
        # connect to the database
        db_name = 'doctor'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
            UPDATE doctor_availability_AM
            SET 
                `{time}` = 1,
                `{time_id}` = '{patient}' 
            WHERE bookingDate = '{date}' AND doctor = '{doctor}'
            """.format(time=time, time_id=time + '-patient-id', patient=patient, date=_date, doctor=doctor)

        cur.execute(query)
        db_connection.commit()
        cur.close()

    except Exception:
        raise DbConnectionError("Failed to connect to the database")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


def delete_booking(booking_date, time_slot_column_name, patientID):
    try:
        db_connection = mysql.connector.connect(
            host=HOST,
            user=USERNAME,
            password=PASSWORD,
            database="doctor"
        )
        cur = db_connection.cursor()
        print("connected")
        query = """
        UPDATE doctor_availability_AM
        SET 
            `{time_slot_column_name}` = NULL,
            `{time_slot_id_column_name}` = NULL
        WHERE bookingDate = '{booking_date}' AND `{time_slot_id_column_name}` = '{patientID}';
        """.format(time_slot_column_name=time_slot_column_name,
                   time_slot_id_column_name=time_slot_column_name + '-patient-id',
                   booking_date=booking_date, patientID=patientID)

        cur.execute(query)
        db_connection.commit()

        print("Booking deleted successfully")
        cur.close()
    except mysql.connector.Error as err:
        raise DbConnectionError(f"Failed to connect to the database: {err}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Get available doctors so we can randomise which doctor is assigned to appointment
def get_available_doctors(_date, time):
    try:
        db_name = 'doctor'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
           SELECT  Doctor
            FROM doctor_availability_AM 
            WHERE bookingDate = '{}' AND `{}` IS null ;
            """.format(_date, time)

        cur.execute(query)

        results = cur.fetchall()  # this is a list with db records where each record is a tuple
        doctors_available = [item[0] for item in results]

        for i in doctors_available:
            print(i)

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return doctors_available


# Getting patient ID from DOB and Surname
def getPatientID(patient_DOB, patient_surname):
    try:
        db_name = 'doctor'
        db_connection = _connect_to_db(db_name)
        cur = db_connection.cursor()
        print("Connected to DB: %s" % db_name)

        query = """
           SELECT  patient_id
            FROM patient_records
            WHERE patient_DOB = '{}' AND patient_surname = '{}';
            """.format(patient_DOB, patient_surname)

        cur.execute(query)

        results = cur.fetchall()

        cur.close()

    except Exception:
        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")

    return results
