# cli/event_cli.py
from models.event import Event
# from models.base import session
from planner.cli.database_setup import Session

class EventCLI:
    def menu(self):
        session = Session()
        while True:
            print("\nEvent Menu:")
            print("1. Create Event")
            print("2. Delete Event")
            print("3. View All Events")
            print("4. Find Event by ID")
            print("5. Back to Main Menu")

            choice = input("Choose an option: ")

            if choice == '1':
                self.create_event(session)
            elif choice == '2':
                self.delete_event(session)
            elif choice == '3':
                self.view_all_events(session)
            elif choice == '4':
                self.find_event_by_id(session)
            elif choice == '5':
                break
            else:
                print("Invalid choice, please try again.")

    def create_event(self):
        try:
            name = input("Event Name: ")
            description = input("Event Description: ")
            event_date = input("Event Date (YYYY-MM-DD): ")
            event_time = input("Event Time (HH:MM:SS): ")
            if not name or not event_date or not event_time:
                raise ValueError("Event Name, Date, and Time are required.")
            
            event = Event(
                event_name=name,
                event_description=description,
                event_date=event_date,
                event_time=event_time
            )
            session.add(event)
            session.commit()
            print("Event created successfully.")
        except ValueError as ve:
            print(f"Validation error: {ve}")
        except Exception as e:
            print(f"Error creating event: {e}")

    def delete_event(self):
        try:
            event_id = int(input("Enter Event ID to delete: "))
            event = session.query(Event).get(event_id)
            if event:
                session.delete(event)
                session.commit()
                print("Event deleted successfully.")
            else:
                print("Event not found.")
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
        except Exception as e:
            print(f"Error deleting event: {e}")

    def view_all_events(self):
        try:
            events = session.query(Event).all()
            if events:
                for event in events:
                    print(f"ID: {event.event_id}, Name: {event.event_name}, Description: {event.event_description}")
            else:
                print("No events found.")
        except Exception as e:
            print(f"Error retrieving events: {e}")

    def find_event_by_id(self):
        try:
            event_id = int(input("Enter Event ID: "))
            event = session.query(Event).get(event_id)
            if event:
                print(f"ID: {event.event_id}, Name: {event.event_name}, Description: {event.event_description}")
            else:
                print("Event not found.")
        except ValueError:
            print("Invalid ID. Please enter a numeric value.")
        except Exception as e:
            print(f"Error finding event: {e}")

if __name__ == "__main__":
    EventCLI().menu()

