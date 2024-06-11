# cli/event_venue_cli.py

from models.event_venue import EventVenue
from models.base import session

class EventVenueCLI:
    def menu(self):
        while True:
            print("\nEvent Venue Menu:")
            print("1. Create Event Venue")
            print("2. Delete Event Venue")
            print("3. View All Event Venues")
            print("4. Find Event Venue by ID")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == '1':
                self.create_event_venue()
            elif choice == '2':
                self.delete_event_venue()
            elif choice == '3':
                self.view_all_event_venues()
            elif choice == '4':
                self.find_event_venue_by_id()
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

    def create_event_venue(self):
        try:
            event_id = int(input("Enter Event ID: "))
            venue_id = int(input("Enter Venue ID: "))
            setup_start_time = input("Enter Setup Start Time (HH:MM:SS): ")
            cleanup_end_time = input("Enter Cleanup End Time (HH:MM:SS): ")

            event_venue = EventVenue(
                event_id=event_id,
                venue_id=venue_id,
                setup_start_time=setup_start_time,
                cleanup_end_time=cleanup_end_time
            )
            session.add(event_venue)
            session.commit()
            print("Event Venue created successfully.")
        except ValueError:
            print("Invalid input. Please enter numeric values for Event ID and Venue ID.")
        except Exception as e:
            print(f"Error creating Event Venue: {e}")

    def delete_event_venue(self):
        try:
            event_venue_id = int(input("Enter Event Venue ID to delete: "))
            event_venue = session.query(EventVenue).get(event_venue_id)
            if event_venue:
                session.delete(event_venue)
                session.commit()
                print("Event Venue deleted successfully.")
            else:
                print("Event Venue not found.")
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
        except Exception as e:
            print(f"Error deleting Event Venue: {e}")

    def view_all_event_venues(self):
        try:
            event_venues = session.query(EventVenue).all()
            if event_venues:
                for event_venue in event_venues:
                    print(f"ID: {event_venue.event_venue_id}, Event ID: {event_venue.event_id}, Venue ID: {event_venue.venue_id}, Setup Start Time: {event_venue.setup_start_time}, Cleanup End Time: {event_venue.cleanup_end_time}")
            else:
                print("No Event Venues found.")
        except Exception as e:
            print(f"Error retrieving Event Venues: {e}")

    def find_event_venue_by_id(self):
        try:
            event_venue_id = int(input("Enter Event Venue ID: "))
            event_venue = session.query(EventVenue).get(event_venue_id)
            if event_venue:
                print(f"ID: {event_venue.event_venue_id}, Event ID: {event_venue.event_id}, Venue ID: {event_venue.venue_id}, Setup Start Time: {event_venue.setup_start_time}, Cleanup End Time: {event_venue.cleanup_end_time}")
            else:
                print("Event Venue not found.")
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
        except Exception as e:
            print(f"Error finding Event Venue: {e}")

if __name__ == "__main__":
    EventVenueCLI().menu()
