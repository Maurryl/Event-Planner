# cli/venue_cli.py
from models.venue import Venue
from models.base import session

class VenueCLI:
    def menu(self):
        while True:
            print("\nVenue Menu:")
            print("1. Create Venue")
            print("2. Delete Venue")
            print("3. View All Venues")
            print("4. Find Venue by ID")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == '1':
                self.create_venue()
            elif choice == '2':
                self.delete_venue()
            elif choice == '3':
                self.view_all_venues()
            elif choice == '4':
                self.find_venue_by_id()
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

    def create_venue(self):
        name = input("Venue Name: ")
        location = input("Venue Location: ")
        capacity = int(input("Venue Capacity: "))
        contact_person = input("Contact Person: ")
        contact_phone = input("Contact Phone: ")
        rental_cost = float(input("Rental Cost: "))
        availability_status = input("Availability Status: ")
        venue = Venue(
            venue_name=name,
            venue_location=location,
            capacity=capacity,
            contact_person=contact_person,
            contact_phone=contact_phone,
            rental_cost=rental_cost,
            availability_status=availability_status
        )
        session.add(venue)
        session.commit()
        print("Venue created successfully.")

    def delete_venue(self):
        venue_id = input("Enter Venue ID to delete: ")
        venue = session.query(Venue).get(venue_id)
        if venue:
            session.delete(venue)
            session.commit()
            print("Venue deleted successfully.")
        else:
            print("Venue not found.")

    def view_all_venues(self):
        venues = session.query(Venue).all()
        for venue in venues:
            print(f"ID: {venue.venue_id}, Name: {venue.venue_name}, Location: {venue.venue_location}, Capacity: {venue.capacity}")

    def find_venue_by_id(self):
        venue_id = input("Enter Venue ID: ")
        venue = session.query(Venue).get(venue_id)
        if venue:
            print(f"ID: {venue.venue_id}, Name: {venue.venue_name}, Location: {venue.venue_location}, Capacity: {venue.capacity}")
        else:
            print("Venue not found.")
            
if __name__ == "__main__":
    VenueCLI().menu()
