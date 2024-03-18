from flask import *
import json


def provider():
    li1 = []
    dic = {}
    name = input("Doctor name : ").lower()
    specialization = input("Doctor belongs to: ").lower()
    avail = input("Doctor available timings: ")
    li1.append(name)
    li1.append(avail)
    dic[specialization] = li1
    print("Ok your data successfully stored")
    return dic


def patient(file_path):
    doctor = input("Who you want to meet: ").replace(" ", "").lower()
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    if doctor in data.keys():
        print("Doctor for your problem and their available timings are:")
        lst = data.get(doctor)

        def flatten(lst):
            flattened_list = []
            for item in lst:
                if isinstance(item, list):
                    flattened_list += item
                else:
                    flattened_list.append(item)
            return flattened_list

        flattened_list = flatten(data.get(doctor))
        paired_list = zip(flattened_list[::2], flattened_list[1::2])

        for name, value in paired_list:
            print(name, value)

    else:
        return"sorry! doctor not available."


def add_dictionary_to_json_file(file_path, my_dict):
    try:
        with open(file_path, 'r') as json_file:
            existing_data = json.load(json_file)
    except FileNotFoundError:
        existing_data = {}

    for key, value in my_dict.items():
        if key in existing_data:

            if isinstance(existing_data[key], list):
                existing_data[key].append(value)
            else:
                existing_data[key] = [existing_data[key], value]
        else:
            existing_data[key] = value

    with open(file_path, 'w') as json_file:
        json.dump(existing_data, json_file, indent=2)


def appointment():
    while True:
        print("check doctor availability and book your appointment")
        name = input("Patient Full Name: ")
        age = input("Age:")
        gender = input("MALE/FEMALE/OTHER:")
        mobile = input("Mobile Number:")
        if len(mobile) < 10 or len(mobile) > 10:
            print("mobile number should be 10 digits")
            mobile = v = input("Enter mobile number again:")

        doctor = input("Who you want to meet:")
        time = input("Time of appointment:")
        break
    print("YOUR APPOINTMENT HAS BOOKED VISIT BEFORE TIME")
    a_dict = {}
    a_dict[mobile] = [name, age, gender, doctor, time]

    try:
        with open(file_path2, 'r') as json_file2:
            existing_data = json.load(json_file2)
    except FileNotFoundError:
        existing_data = {}
    existing_data.update(a_dict)

    with open(file_path2, 'w') as json_file2:
        json.dump(existing_data, json_file2, indent=2)


def cancel_appointment():
    print("To cancel your appointment please enter your mobile number:")
    mobile = input()
    with open(file_path2, 'r') as file2:
        data1 = json.load(file2)
        if not file_path2:
            print("nothing to clear")
        if mobile in data1.keys():
            del data1[mobile]
            with open(file_path2, 'w') as json_file2:
                json.dump(data1, json_file2, indent=2)
            print("Your appointment has been successfully canceled.")
        else:
            print("No appointment found for the provided mobile number.")


# def remove_dr():
#     print("enter dr")


my_dict = {}
file_path = 'data.json'
file_path2 = 'AP.json'




while True:
        print("if nothing enter end")
        role = input("enter your role: ").replace(" ", "").lower()
        if role == "provider":
            check = input("New entry/Remove:").replace(" ", "").lower()
            if check == "newentry":
                my_dict.update(provider())
                add_dictionary_to_json_file(file_path, my_dict)
            # elif check =="remove":
        elif role == "patient":
            checking = input("Dr.Avail/Appointment/Cancel AP:").replace(" ", "").lower()
            if checking == "da":
                if not file_path:
                    print("User has not provided data.")
                    break
                patient(file_path)
            elif checking == "appointment":
                appointment()
            elif checking == "cancel":
                cancel_appointment()
            else:
                print("invalid entry!!")

        elif role == "end":
            print("Thank you")
            break

        else:
            print("Invalid entry!")
