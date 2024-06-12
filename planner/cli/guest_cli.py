# cli/guest_cli.py
from models.guest import Guest
from models.base import session

class GuestCLI:
    def menu(self):
        while True:
            print("\nGuest Menu:")
            print("1. Create Guest")
            print("2. Delete Guest")
            print("3. View All Guests")
            print("4. Find Guest by ID")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == '1':
                self.create_guest()
            elif choice == '2':
                self.delete_guest()
            elif choice == '3':
                self.view_all_guests()
            elif choice == '4':
                self.find_guest_by_id()
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

    def create_guest(self):
        try:
            name = input("Guest Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            event_id = int(input("Event ID: "))
            rsvp_status = input("RSVP Status (Attending, Not Attending, Maybe): ")
            invitation_sent = input("Invitation Sent (True/False): ").lower() == 'true'
            special_requests = input("Special Requests: ")
            if not name or not email:
                raise ValueError("Guest Name and Email are required.")

            guest = Guest(
                guest_name=name,
                email=email,
                phone=phone,
                event_id=event_id,
                rsvp_status=rsvp_status,
                invitation_sent=invitation_sent,
                special_requests=special_requests
            )
            session.add(guest)
            session.commit()
            print("Guest created successfully.")
        except ValueError as ve:
            print(f"Validation error: {ve}")
        except Exception as e:
            print(f"Error creating guest: {e}")

    def delete_guest(self):
        try:
            guest_id = int(input("Enter Guest ID to delete: "))
            guest = session.query(Guest).get(guest_id)
            if guest:
                session.delete(guest)
                session.commit()
                print("Guest deleted successfully.")
            else:
                print("Guest not found.")
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
        except Exception as e:
            print(f"Error deleting guest: {e}")

    def view_all_guests(self):
        try:
            guests = session.query(Guest).all()
            if guests:
                for guest in guests:
                    print(f"ID: {guest.guest_id}, Name: {guest.guest_name}, Email: {guest.email}")
            else:
                print("No guests found.")
        except Exception as e:
            print(f"Error retrieving guests: {e}")

    def find_guest_by_id(self):
        try:
            guest_id = int(input("Enter Guest ID: "))
            guest = session.query(Guest).get(guest_id)
            if guest:
                print(f"ID: {guest.guest_id}, Name: {guest.guest_name}, Email: {guest.email}")
            else:
                print("Guest not found.")
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
        except Exception as e:
            print(f"Error finding guest: {e}")

if __name__ == "__main__":
    GuestCLI().menu()

