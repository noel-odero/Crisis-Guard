#!/usr/bin/python3

from crisis_guard import *


def main_menu():
    """
    Display the main menu and handle user input to navigate to different functionalities.
    """
    while True:
        # Display the menu options
        print("\nWelcome to CrisisGuard -This is  a Community Support System")
        print("1. Report a Medical Emergency")
        print("2. Request Legal Assistance")
        print("3. Report an Incident")
        print("4. Volunteer Opportunities")
        print("5. Community Events")
        print("6. Local Resources Directory")
        print("7. Educational Workshops and Webinars")
        print("8. Exit")

         # Get user choice
        choice = input("Enter your choice: ")

         # Call the appropriate function based on user choice
        if choice == '1':
            report_medical_emergency()
        elif choice == '2':
            request_legal_assistance()
        elif choice == '3':
            report_incident()
        elif choice == '4':
            volunteer_opportunities()
        elif choice == '5':
            community_events()
        elif choice == '6':
            local_resources_directory()
        elif choice == '7':
            educational_workshops()
        elif choice == '8':
            print("Exiting the system. Stay safe!")
            break
        else:
            print("Invalid choice, please try again.")

# Start the main menu
if __name__=="__main__":
    main_menu()
