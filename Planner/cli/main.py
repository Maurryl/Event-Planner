# cli/main.py
import sys
from .event_cli import EventCLI
from .guest_cli import GuestCLI
from .venue_cli import VenueCLI

def main():
    while True:
        print("\nMain Menu:")
        print("1. Manage Events")
        print("2. Manage Guests")
        print("3. Manage Venues")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            EventCLI().menu()
        elif choice == '2':
            GuestCLI().menu()
        elif choice == '3':
            VenueCLI().menu()
        elif choice == '4':
            sys.exit()
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
