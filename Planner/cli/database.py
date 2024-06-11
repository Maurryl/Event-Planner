from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.categories import Category
from models.event import Event
from models.guest import Guest
from models.venue import Venue
from models.event_venue import EventVenue

# Create database engine
engine = create_engine('sqlite:///event_planner.db')

# Create a session
Session = sessionmaker(bind=engine)

#Test data
session = Session()

# Sample data for Categories
categories_data = [
    {"name": "Music", "description": "Concerts, festivals, etc."},
    {"name": "Conference", "description": "Business meetings, seminars."},
    {"name": "Wedding", "description": "Wedding ceremonies and receptions."},
    {"name": "Sport", "description": "Sporting events, tournaments."},
    {"name": "Exhibition", "description": "Art exhibitions, trade shows."},
    {"name": "Party", "description": "Social gatherings, celebrations."},
    {"name": "Workshop", "description": "Educational workshops, training sessions."},
    {"name": "Charity", "description": "Fundraising events, charity galas."},
    {"name": "Networking", "description": "Professional networking events."},
    {"name": "Theater", "description": "Theatrical performances, plays."},
]
# # Insert data into Categories table
# for category_info in categories_data:
#     category = Category(**category_info)
#     session.add(category)

# # Commit the changes
# session.commit()

# Sample data for Events
events_data = [
    {"event_name": "Summer Music Festival", "event_description": "Annual music festival featuring various artists.",
     "event_date": datetime(2024, 7, 15), "event_time": datetime.strptime("18:00:00", "%H:%M:%S")},
    {"event_name": "Tech Conference 2024", "event_description": "Leading technology conference with keynote speakers.",
     "event_date": datetime(2024, 9, 20), "event_time": datetime.strptime("09:00:00", "%H:%M:%S")},
    {"event_name": "Jane & John's Wedding", "event_description": "Wedding ceremony and reception for Jane and John.",
     "event_date": datetime(2024, 8, 10), "event_time": datetime.strptime("14:00:00", "%H:%M:%S")},
    {"event_name": "Soccer Tournament", "event_description": "Local soccer tournament for youth teams.",
     "event_date": datetime(2024, 6, 25), "event_time": datetime.strptime("10:00:00", "%H:%M:%S")},
    {"event_name": "Art Expo 2024", "event_description": "Annual art exhibition showcasing local artists.",
     "event_date": datetime(2024, 10, 5), "event_time": datetime.strptime("11:00:00", "%H:%M:%S")},
    {"event_name": "New Year's Eve Party", "event_description": "Celebrate the new year with friends and family.",
     "event_date": datetime(2024, 12, 31), "event_time": datetime.strptime("20:00:00", "%H:%M:%S")},
    {"event_name": "Python Workshop", "event_description": "Hands-on workshop for learning Python programming.",
     "event_date": datetime(2024, 7, 30), "event_time": datetime.strptime("13:00:00", "%H:%M:%S")},
    {"event_name": "Charity Gala Dinner", "event_description": "Fundraising gala dinner for local charity.",
     "event_date": datetime(2024, 9, 15), "event_time": datetime.strptime("19:00:00", "%H:%M:%S")},
    {"event_name": "Business Networking Mixer", "event_description": "Networking event for professionals in various industries.",
     "event_date": datetime(2024, 8, 5), "event_time": datetime.strptime("17:30:00", "%H:%M:%S")},
    {"event_name": "Shakespeare in the Park", "event_description": "Outdoor theatrical performance of Shakespeare's plays.",
     "event_date": datetime(2024, 7, 5), "event_time": datetime.strptime("19:30:00", "%H:%M:%S")},
]

# # Insert data into Events table
# for event_info in events_data:
#     event = Event(**event_info)
#     session.add(event )

# # Commit the changes
# session.commit()

# Sample data for Guests
guests_data = [
    {"guest_name": "John Doe", "email": "john@example.com", "phone": "123-456-7890",
     "rsvp_status": "Attending", "invitation_sent": True, "special_requests": "None", "event_id": 1},
    {"guest_name": "Jane Smith", "email": "jane@example.com", "phone": "987-654-3210",
     "rsvp_status": "Maybe", "invitation_sent": True, "special_requests": "Vegetarian meal", "event_id": 1},
    {"guest_name": "Alice Johnson", "email": "alice@example.com", "phone": "111-222-3333",
     "rsvp_status": "Not Attending", "invitation_sent": True, "special_requests": "Allergic to peanuts", "event_id": 2},
    {"guest_name": "Bob Williams", "email": "bob@example.com", "phone": "444-555-6666",
     "rsvp_status": "Attending", "invitation_sent": True, "special_requests": "None", "event_id": 2},
    {"guest_name": "Emily Davis", "email": "emily@example.com", "phone": "777-888-9999",
     "rsvp_status": "Maybe", "invitation_sent": False, "special_requests": "None", "event_id": 3},
    {"guest_name": "Michael Brown", "email": "michael@example.com", "phone": "999-888-7777",
     "rsvp_status": "Attending", "invitation_sent": True, "special_requests": "None", "event_id": 3},
    {"guest_name": "Emma Martinez", "email": "emma@example.com", "phone": "333-222-1111",
     "rsvp_status": "Maybe", "invitation_sent": True, "special_requests": "None", "event_id": 4},
    {"guest_name": "William Garcia", "email": "william@example.com", "phone": "444-333-2222",
     "rsvp_status": "Attending", "invitation_sent": True, "special_requests": "None", "event_id": 4},
    {"guest_name": "Olivia Rodriguez", "email": "olivia@example.com", "phone": "555-444-3333",
     "rsvp_status": "Not Attending", "invitation_sent": True, "special_requests": "None", "event_id": 5},
    {"guest_name": "James Lee", "email": "james@example.com", "phone": "666-555-4444",
     "rsvp_status": "Attending", "invitation_sent": True, "special_requests": "None", "event_id": 5},
    {"guest_name": "Sophia Harris", "email": "sophia@example.com", "phone": "777-666-5555",
     "rsvp_status": "Maybe", "invitation_sent": True, "special_requests": "None", "event_id": 6},
    {"guest_name": "Benjamin King", "email": "benjamin@example.com", "phone": "888-777-6666",
     "rsvp_status": "Attending", "invitation_sent": True, "special_requests": "None", "event_id": 6},
    
]

# # Insert data into Guests table
# for guest_info in guests_data:
#     guest = Guest(**guest_info)
#     session.add(guest)

# # Commit the changes
# session.commit()

    
# Sample data for Venues
venues_data = [
    {"venue_name": "City Arena", "venue_address": "123 Main St", "capacity": 1000},
    {"venue_name": "Tech Center", "venue_address": "456 Oak Ave", "capacity": 500},
    {"venue_name": "Beachfront Resort", "venue_address": "789 Ocean Blvd", "capacity": 300},
    {"venue_name": "Grand Ballroom", "venue_address": "1010 Broadway", "capacity": 800},
    {"venue_name": "Downtown Theater", "venue_address": "222 Elm St", "capacity": 400},
    {"venue_name": "Conference Hall", "venue_address": "333 Pine Ave", "capacity": 600},
    {"venue_name": "Riverside Park Pavilion", "venue_address": "101 Riverside Dr", "capacity": 200},
    {"venue_name": "The Loft Event Space", "venue_address": "456 Loft St", "capacity": 150},
    {"venue_name": "Garden Terrace", "venue_address": "789 Garden Ave", "capacity": 300},
    {"venue_name": "The Grand Banquet Hall", "venue_address": "1000 Main St", "capacity": 500},
    {"venue_name": "Lakeside Manor", "venue_address": "123 Lakeview Dr", "capacity": 250},
    {"venue_name": "Mountain View Lodge", "venue_address": "456 Mountain Rd", "capacity": 400},
    {"venue_name": "Urban Warehouse", "venue_address": "789 Warehouse Blvd", "capacity": 200},
    {"venue_name": "Golden Ballroom", "venue_address": "1010 Gold St", "capacity": 600},
    {"venue_name": "Skyline Rooftop", "venue_address": "123 Skyline Ave", "capacity": 300},
    {"venue_name": "Community Center", "venue_address": "456 Community St", "capacity": 200},
]

# # Insert data into Venues table
# for venue_info in venues_data:
#     venue = Venue(**venue_info)
#     session.add(venue)

# # Commit the changes
# session.commit()



# Sample data for EventVenues
event_venues_data = [
    {"event_id": 1, "venue_id": 1, "setup_start_time": datetime.strptime("16:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("23:00:00", "%H:%M:%S")},
    {"event_id": 2, "venue_id": 2, "setup_start_time": datetime.strptime("08:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("17:00:00", "%H:%M:%S")},
    {"event_id": 3, "venue_id": 3, "setup_start_time": datetime.strptime("12:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("01:00:00", "%H:%M:%S")},
    {"event_id": 4, "venue_id": 4, "setup_start_time": datetime.strptime("09:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("18:00:00", "%H:%M:%S")},
    {"event_id": 5, "venue_id": 5, "setup_start_time": datetime.strptime("10:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("22:00:00", "%H:%M:%S")},
    {"event_id": 6, "venue_id": 6, "setup_start_time": datetime.strptime("14:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("23:00:00", "%H:%M:%S")},
    {"event_id": 7, "venue_id": 7, "setup_start_time": datetime.strptime("11:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("20:00:00", "%H:%M:%S")},
    {"event_id": 8, "venue_id": 8, "setup_start_time": datetime.strptime("16:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("01:00:00", "%H:%M:%S")},
    {"event_id": 9, "venue_id": 9, "setup_start_time": datetime.strptime("17:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("23:59:59", "%H:%M:%S")},
    {"event_id": 10, "venue_id": 10, "setup_start_time": datetime.strptime("15:00:00", "%H:%M:%S"), "cleanup_end_time": datetime.strptime("22:00:00", "%H:%M:%S")},
]

# # Insert data into EventVenues table
# for event_venue_info in event_venues_data:
#     event_venue = EventVenue(**event_venue_info)
#     session.add(event_venue)

# # Commit the changes
# session.commit()


# Create test data

event = Event(**events_data)

category = Category(**categories_data)

guest = Guest(**guests_data)

venue = Venue(**venues_data)

event_venue = EventVenue (**event_venues_data)


# Add data to the session

session.add(event)

session.add(category)

session.add(guest)

session.add(venue)

session.add(event_venue)


# Commit the session

session.commit()


# Test relationships

event.venue = venue

session.commit()


# Query the data

events = session.query(Event).all()

categories = session.query(Category).all()

guests = session.query(Guest).all()

venues = session.query(Venue).all()

event_venues = session.query(EventVenue).all()


# Print the results

print("Categories:")

for category in categories:

    print(category)


print("\nEvents:")

for event in events:

    print(event)


print("\nGuests:")

for guest in guests:

    print(guest)


print("\nVenues:")

for venue in venues:

    print(venue)

print("\nEvent_Venues:")

for event_venue in event_venues:

    print(event_venue)

# Close the session

session.close()