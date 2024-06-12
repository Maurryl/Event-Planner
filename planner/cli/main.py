
# import sys
# from .event_cli import EventCLI
# from .guest_cli import GuestCLI
# from .venue_cli import VenueCLI



# def main():
#     while True:
#         print("\nMain Menu:")
#         print("1. Manage Events")
#         print("2. Manage Guests")
#         print("3. Manage Venues")
#         print("4. Exit")

#         choice = input("Choose an option: ")

#         if choice == '1':
#             EventCLI().menu()
#         elif choice == '2':
#             GuestCLI().menu()
#         elif choice == '3':
#             VenueCLI().menu()
#         elif choice == '4':
#             sys.exit()
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == '__main__':
#     main()



from cli.category_cli import category_menu
from cli.event_cli import event_menu
from cli.guest_cli import guest_menu
from cli.venue_cli import venue_menu
from cli.event_venue_cli import event_venue_menu

def main():
    while True:
        print("Event Planner CLI")
        print("1. Manage Categories")
        print("2. Manage Events")
        print("3. Manage Guests")
        print("4. Manage Venues")
        print("5. Manage Event Venues")
        print("6. Exit")

        choice = input("Enter your choice: ")
        
        if choice == '1':
            category_menu()
        elif choice == '2':
            event_menu()
        elif choice == '3':
            guest_menu()
        elif choice == '4':
            venue_menu()
        elif choice == '5':
            event_venue_menu()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
