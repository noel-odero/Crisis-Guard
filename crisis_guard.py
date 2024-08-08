#!/usr/bin/env python3

import json
import os

DATA_DIR = 'data'


def save_to_json_file(my_obj, filename):
    """
    Writes an Object to a text file, using a JSON representation.
    """
    with open(os.path.join(DATA_DIR, filename), 'w') as f:
        json.dump(my_obj, f)

def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.
    """
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path) or os.stat(file_path).st_size == 0:
        return []
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def ensure_data_directory():
    """
    Ensure that the data directory exists.
    """
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def report_medical_emergency():
    print("\nReporting a Medical Emergency\n")

    # Collecting information about the user
    user_name = input("What is your name? ")
    location = input("What is your location? ")
    prompt = f"{user_name}, are you reaching out for yourself or someone else?\n"
    prompt += "Please choose:\n"
    prompt += "1- Self\n"
    prompt += "2- Others\n"

    relation_to_victim = input(prompt).strip().lower()

    emergency_details = {
        "user_name": user_name,
        "location": location,
        "relation_to_victim": relation_to_victim,
        "situation_description": "",
        "other_description": ""
    }
    # Scenario 1: The victim is the one calling
    if relation_to_victim == "1":
        print("What happened?")
        print("1- I have been shot")
        print("2- I have been exposed to tear gas")
        print("3- I am badly burned")
        print("4- I have been exposed to a chemical")
        print("5- Other (please describe)")
        situation_description = input("Please select one number above: ").strip().lower()

        # Handling the different cases when the victim is the one calling:
        if situation_description == "1":
            emergency_details["situation_description"] = "shot"
            print(f"{user_name}, you have been shot. Apply pressure to the wound with a clean cloth or bandage to control bleeding. Do not remove any objects stuck in the wound. If you can, call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        elif situation_description == "2":
            emergency_details["situation_description"] = "exposed to tear gas"
            print(f"{user_name}, you have been exposed to tear gas. Leave the vicinity of tear gas as swiftly as possible to reduce exposure. Upon reaching fresh air, rinse your eyes and face with water to mitigate irritation. Avoid rubbing your face and ensure the water flows off without re-entering your eyes. Call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        elif situation_description == "3":
            emergency_details["situation_description"] = "badly burned"
            print(f"{user_name}, you are badly burned. Move to a safe, cool environment away from the source of the fire. Call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        elif situation_description == "4":
            emergency_details["situation_description"] = "exposed to a chemical"
            print(f"{user_name}, you have been exposed to a chemical. If you have breathed in the chemical, immediately move to fresh air. If this chemical contacts the skin, flush the contaminated skin with water promptly. If the chemical has been ingested, call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        elif situation_description == "5":
            other_description = input("Please describe your situation: ")
            print(f"{user_name}, call 112 immediately and inform them of the situation. We have also connected you to emergency services. Everything will be alright, take deep breaths and stay calm.")

        else:
            print("Invalid selection. Please try again.")

    # Scenario 2: The victim is not the one calling
    elif relation_to_victim == "2":
        print(f"\nChoose the option that describes the emergency:\n")
        print("1. The person has been shot")
        print("2. The person is unconscious")
        print("3. The person is choking")
        print("4. The person is having difficulty breathing")
        print("5. The person has been in contact with chemicals")
        print("6. Other (please describe)")

        # Getting the user's choice
        emergency_choice = input(f"{user_name}, please enter the corresponding number for the emergency: ").strip()

        # Handling different emergency scenarios when the victim is not the one calling
        if emergency_choice == '1':
            emergency_details["situation_description"] = "shot"
            print(f"\n{user_name}, for a gunshot wound, apply pressure to the wound with a clean cloth or bandage to control bleeding. Do not remove any objects stuck in the wound. Call 112 immediately and inform them of the situation. We have also connected you to emergency services.")

        elif emergency_choice == '2':
            emergency_details["situation_description"] = "unconscious"
            print(f"\n{user_name}, for an unconscious person, check if they are responsive. If not, roll them onto their side to prevent choking on vomit or saliva. Call 112 immediately. We have also connected you to emergency services.")

        elif emergency_choice == '3':
            emergency_details["situation_description"] = "choking"
            print(f"\n{user_name}, for choking, perform the Heimlich maneuver (if you have been trained) if the person is unable to breathe. Call 112 immediately after performing the maneuver. We have also connected you to emergency services.")

        elif emergency_choice == '4':
            emergency_details["situation_description"] = "difficulty breathing"
            print(f"\n{user_name}, for difficulty breathing, sit the person upright and keep them comfortable. Administer oxygen if available. Call 112 immediately. We have also connected you to emergency services.")

        elif emergency_choice == '5':
            emergency_details["situation_description"] = "chemical exposure"
            print(f"\n{user_name}, for exposure to poisonous chemicals, if the person has breathed in a chemical, immediately move them to fresh air. If this chemical touched the skin, flush the contaminated skin with water promptly. If the chemical has been ingested, call 112 immediately and inform them of the situation. We have also connected you to emergency services.")

        elif emergency_choice == '6':
            emergency_details["situation_description"] = "other"
            other_description = input(f"{user_name}, please describe the emergency: ").strip()
            print(f"\n{user_name}, for '{other_description}', here are some general steps: Call 112 immediately and stay on the line with the dispatcher. They will guide you through the initial steps until help arrives. We have also connected you to emergency services.")

        else:
            print(f"\n{user_name}, invalid option selected. Please try again.")

    # A wrong option has been selected
    else:
        print("Invalid selection. Please select between 1 and 2. Note that the emergency number is 112.")
    data = load_from_json_file("medical_emergencies.json")
    data.append(emergency_details)
    save_to_json_file(data, "medical_emergencies.json")

""" Script to record brutality incidents """


def report_incident():
    """Gathers information about the brutality incident from the user"""
    user_info = {}

    user_info['location'] = input("Where is the incident venue? Please give a location or a landmark within 1km if you are in doubt: ")

    # Prompt the user to specify when the incident occurred
    date_prompt = "Please choose one of the following options:\n"
    date_prompt += "1. The incident is happening now. I require immediate assistance.\n"
    date_prompt += "2. The incident is happening now. I do not need immediate assistance.\n"
    date_prompt += "3. The incident took place in the past."
    user_info['date'] = input(date_prompt)

    # Prompt the user to specify their role in the incident
    role_prompt = "Please choose one of the following options:\n"
    role_prompt += "1. I am the victim\n"
    role_prompt += "2. I am a witness\n"
    role_prompt += "3. I am a culprit"
    user_info['role'] = input(role_prompt)

    # Prompt the user to describe the situation
    user_info['situation_description'] = input("Please briefly describe the incident. Do not leave out any details. Specify the date or period if the incident took place in the past: ")

    # Displays a summary of the gathered information
    print("\nSummary of the information provided:")
    print(f"Date: {user_info['date']}")
    print(f"Location: {user_info['location']}")
    print(f"Role in the event: {user_info['role']}")
    print(f"This is what happened: {user_info['situation_description']}")

    # Provide emergency contact information if the incident is happening now
    if user_info['date'] == '1':
        print("\nCall one of the following services according to your need:\nPolice: 999\nEmergency: 911\nFire department: 112")
    data = load_from_json_file("incidents.json")
    data.append(user_info)
    save_to_json_file(data, "incidents.json")

    print("Thank you for reporting this incident. You will receive updates on progress when we start examining your case.")

""" This function is to inform about the workshops and webinars available. """
def educational_workshops():
    """
    Loads existing educational workshops and webinars from a JSON file, displays them to the user,
    and allows the user to add new workshops or webinars, which are then saved back to the JSON file.
    """
    print("Accessing Educational Workshops and Webinars...")
    workshops = load_from_json_file("educational_workshops.json")
    for idx, workshop in enumerate(workshops, start=1):
        print(f"{idx}. {workshop}")

    new_workshop = input("Enter a new workshop or webinar (or press Enter to skip): ")
    if new_workshop:
        workshops.append(new_workshop)
        save_to_json_file(workshops, "educational_workshops.json")
        print("Workshop or webinar added successfully.")


def request_legal_assistance():
    print("\nRequesting Legal Assistance\n")

    # Collecting information about the user
    user_name = input("What is your name? ")
    location = input("What is your location? ")
    contact_details = input("Enter your contact details: ")

    # Asking about the nature of the legal issue
    print("\nPlease describe the nature of your legal issue:")
    print("1. Arrest/Detention")
    print("2. Property Dispute")
    print("3. Employment Issue")
    print("4. Discrimination or Harassment")
    print("5. Other (please describe)")

    legal_issue = input("Please select one number above: ").strip().lower()

    legal_details = {
        "user_name": user_name,
        "location": location,
        "contact_details": contact_details,
        "legal_issue": "",
        "other_issue": ""
    }

    # Handling the different cases for the legal issue
    if legal_issue == "1":
        legal_details["legal_issue"] = "Arrest/Detention"
        print(f"{user_name}, we have recorded your request for legal assistance regarding an arrest or detention. Our legal team will contact you at {contact_details} to provide support.")

    elif legal_issue == "2":
        legal_details["legal_issue"] = "Property Dispute"
        print(f"{user_name}, we have recorded your request for legal assistance regarding a property dispute. Our legal team will contact you at {contact_details} to provide support.")

    elif legal_issue == "3":
        legal_details["legal_issue"] = "Employment Issue"
        print(f"{user_name}, we have recorded your request for legal assistance regarding an employment issue. Our legal team will contact you at {contact_details} to provide support.")

    elif legal_issue == "4":
        legal_details["legal_issue"] = "Discrimination or Harassment"
        print(f"{user_name}, we have recorded your request for legal assistance regarding discrimination or harassment. Our legal team will contact you at {contact_details} to provide support.")

    elif legal_issue == "5":
        other_issue = input("Please describe your legal issue: ")
        legal_details["legal_issue"] = "Other"
        legal_details["other_issue"] = other_issue
        print(f"{user_name}, we have recorded your request for legal assistance regarding '{other_issue}'. Our legal team will contact you at {contact_details} to provide support.")

    else:
        print("Invalid selection. Please try again.")
        return

    data = load_from_json_file("legal_assistance.json")
    data.append(legal_details)
    save_to_json_file(data, "legal_assistance.json")


def volunteer_opportunities():
    print("\nDo you want to volunteer with us?")
    print("1. Community Clean-Up")
    print("2. Food Distribution")
    print("3. Legal assistant")
    print("4. Medic")
    choice = input("Choose an opportunity to volunteer for (enter the number): ").strip()
    name = input("Enter your name: ").strip()
    contact_details = input("Enter your contact details: ").strip()

    # Mapping the user's choice to the corresponding opportunity
    opportunities_dict = {
        "1": "Community Clean-Up",
        "2": "Food Distribution",
        "3": "Legal Assistance",
        "4": "Medic"
    }

    if choice in opportunities_dict:
        selected_opportunity = opportunities_dict[choice]
        print(f"Thank you, {name}. You have signed up for the volunteer opportunity '{selected_opportunity}'. We will contact you at {contact_details}.")

        # Load existing volunteer opportunities and append the new one
        opportunities = load_from_json_file("volunteer_opportunities.json")
        new_entry = {
            "name": name,
            "contact": contact_details,
            "opportunity": selected_opportunity
        }
        opportunities.append(new_entry)

        # Save the updated list back to the JSON file
        save_to_json_file(opportunities, "volunteer_opportunities.json")

    else:
        print("Invalid choice, please try again.")

def community_events():
    """
    Loads existing community events from a JSON file, displays them to the user,
    and allows the user to add new events, which are then saved back to the JSON file.
    """
    print("Viewing Community Events...")
    events = load_from_json_file("community_events.json")
    for idx, event in enumerate(events, start=1):
        print(f"{idx}. {event}")

    new_event = input("Enter a new community event (or press Enter to skip): ")
    if new_event:
        events.append(new_event)
        save_to_json_file(events, "community_events.json")
        print("Community event added successfully.")


def local_resources_directory():
    """
    Displays a list of local resource categories and allows the user to get more details
    or add new resources. Saves new resources to a JSON file.
    """
    print("\nLocal Resources Directory")
    print("1. Shelters")
    print("2. Food Banks")
    print("3. Mental Health Services")
    print("4. View all local resources")
    print("5. Add a new local resource")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        print("\n Shelters:")
        print("- Community Shelter: 123 Main St, Phone: 555-1234\n")
    elif choice == '2':
        print("\n Food Banks:")
        print("- City Food Bank: 456 Elm St, Phone: 555-5678\n")
    elif choice == '3':
        print("\nMental Health Services:")
        print("- Wellness Center: 789 Oak St, Phone: 555-9012\n")
    elif choice == '4':
        print("\nViewing all local resources...")
        resources = load_from_json_file("local_resources.json")
        if resources:
            for idx, resource in enumerate(resources, start=1):
                print(f"{idx}. {resource}")
        else:
            print("\n❌No resources found.\n")
    elif choice == '5':
        new_resource = input("Enter a new local resource: ")
        if new_resource:
            resources = load_from_json_file("local_resources.json")
            resources.append(new_resource)
            save_to_json_file(resources, "local_resources.json")
            print("Local resource added successfully.")
    else:
        print("Invalid choice, please try again.")
