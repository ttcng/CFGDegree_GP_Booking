# Front end for patient input
import requests
import json
import random # to get random doctors

def add_patient(surname, firstname, DOB, gender):
    patient = {
        "surname": surname,
        "firstname": firstname,
        "DOB": DOB,
        "gender": gender,
    }

    # A put request
    result = requests.post(
        'http://127.0.0.1:5001/add_patient',
        headers={'content-type': 'application/json'},
        data=json.dumps(patient)
    )
    print(result.text)
    return

def display_availability(records):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        'NAME', '08:00-08:15', '08:15-08:30', '08:30-08:45', '08:45-09:00', '09:00-09:15', '09:15-09:30', '09:30-09:45', '09:45-10:00',
        '10:00-10:15', '10:15-10:30', '10:30-10:45', '10:45-11:00', '11:00-11:15', '11:15-11:30', '11:30-11:45', '11:45-12:00'))
    print('-' * 270)

    # print each data item.
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
            item['Doctor'], item['08:00-08:15'], item['08:15-08:30'], item['08:30-08:45'], item['08:45-09:00'],
            item['09:00-09:15'], item['09:15-09:30'], item['09:30-09:45'], item['09:45-10:00'], item['10:00-10:15'],
            item['10:15-10:30'], item['10:30-10:45'], item['10:45-11:00'], item['11:00-11:15'], item['11:15-11:30'],
            item['11:30-11:45'], item['11:45-12:00']
        ))

# Displaying availability for booking appointment:
def get_availability_by_date(date):
    result = requests.get(
        'http://127.0.0.1:5001/availability/{}'.format(date),
        headers={'content-type': 'application/json'}
    )
    return result.json()

def get_patient_ID(patient_DOB, patient_surname):
    patientID = requests.get(
        'http://127.0.0.1:5001/patientID/{}/{}'.format(patient_DOB, patient_surname))
    patientID_json = patientID.json()

    return patientID_json[0][0]


def book_appointment(date, time, patient_DOB, patient_surname):
    # Function to get patient ID from DOB and surname, returns ID
    patientID = get_patient_ID(patient_DOB, patient_surname)

    doctors = requests.get(
        'http://127.0.0.1:5001/availableDoctors/{}/{}'.format(date,time))
    doctors_json = doctors.json()

    doctor = random.choice(doctors_json)
    print(doctor)

    booking = {
        "_date": date,
        "doctor": doctor,
        "time": time,
        "patient": patientID,
    }

    result = requests.put(
        'http://127.0.0.1:5001/booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )
    print(result.text)
    print("Booking is Successful")
    return result.json()

# Delete a booking
def cancel_booking(date, time, patient_DOB, patient_surname):
    # Function to get patient ID from DOB and surname, returns ID
    patientID = get_patient_ID(patient_DOB, patient_surname)

    booking = {
        "booking_date": date,
        "time_slot_column_name": time,
        "patientID": patientID,
    }

    # A put request
    result = requests.put(
        'http://127.0.0.1:5001/cancel_booking',
        headers={'content-type': 'application/json'},
        data=json.dumps(booking)
    )
    print(result.text)
    print()
    print('Your booking has been deleted.')
    return result.json()

#######################################################################################
# Functions for running client side


# Checking patient input when choosing option 1 or 2
class incorrect_input_type(Exception):
    pass
def option1_or2():
    option = input('Please choose Option 1 or 2: ')
    try:
        chosen_option = int(option)
        if chosen_option not in (1, 2):
            print("Please choose either 1 or 2.")
            chosen_option = None
    except:
        raise incorrect_input_type
        chosen_option = None
    finally:
        return chosen_option

# Function for if it is staff accessing
def staff_function():
    password = None
    while password is None:
        password = input('Please input staff password: ')
        if password == "Staff123#":
            date = input("Please input the date you want to check (YYYY-MM-DD): ")
            schedule = get_availability_by_date(date)
            print('####### AVAILABILITY #######')
            print()
            display_availability(schedule)
            print()
        else:
            password = None
    return


# Client side run function
def run():
    print('############################')
    print("Hello, are you patient or staff? \n"
          "Option 1: I am a patient. \n"
          "Option 2: I am staff.")
    print('############################')
    print()
    staff_or_patient = None
    while staff_or_patient is None:
        staff_or_patient = option1_or2()

    # Staff first
    if staff_or_patient == 2:
        staff_function()

    else:
        print('############################')
        print('Hello, how can we help today? \n'
              'Option 1: I am an existing patient. \n'
              'Option 2: I am a new patient.')
        print('############################')
        print()
        option = None
        while option is None:
            option = option1_or2()


        # Existing patient
        if option == 1:

            patient_DOB = input("Please input your date of birth (YYYY-MM-DD): ")
            patient_surname = input("Please type your surname: ")

            print('What can we do for you today? \n'
                  'Option 1: Book an appointment \n'
                  'Option 2: Cancel an appointment \n')
            patient_option = None
            while patient_option is None:
                patient_option = option1_or2()

            # Patient wants to book appointment
            book = patient_option == 1
            if book:
                # Dates are from 20231023, 20231027
                booking_date = input('What date you would like to book your appointment for (YYYY-MM-DD): ')
                booking_time = input('Please type a time slot: \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format('08:00-08:15', '08:15-08:30', '08:30-08:45', '08:45-09:00', '09:00-09:15', '09:15-09:30', '09:30-09:45', '09:45-10:00',
        '10:00-10:15', '10:15-10:30', '10:30-10:45', '10:45-11:00', '11:00-11:15', '11:15-11:30', '11:30-11:45', '11:45-12:00'))

                book_appointment(booking_date, booking_time, patient_DOB, patient_surname)

            # Patient cancel appointment
            else:
                cancel_date = input("What date was your appointment on (YYYY-MM-DD): ")
                cancel_time = input(
                    'Please type your appointment time slot: \n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
                        '08:00-08:15', '08:15-08:30', '08:30-08:45', '08:45-09:00', '09:00-09:15', '09:15-09:30',
                        '09:30-09:45', '09:45-10:00',
                        '10:00-10:15', '10:15-10:30', '10:30-10:45', '10:45-11:00', '11:00-11:15', '11:15-11:30',
                        '11:30-11:45', '11:45-12:00'))

                cancel_booking(cancel_date, cancel_time, patient_DOB, patient_surname)

        # Old patient
        else:
            print("Welcome to the MTANK GP service! \n"
                  "Please provide your details below:")
            new_surname = input('Please type your surname: ')
            new_firstname = input('Please type your first name: ')
            new_DOB = input('Please type your date of birth (YYYY-MM-DD): ')
            new_gender = input('Please type your gender (female/male/other): ')
            add_patient(new_surname, new_firstname, new_DOB, new_gender)


    print()
    print('Thank you for your updates!')



if __name__ == '__main__':
    run()

