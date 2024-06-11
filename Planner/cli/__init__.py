
# cli/__init__.py

# Import all CLI modules
from .main import main
from .event_cli import EventCLI
from .guest_cli import GuestCLI
from .venue_cli import VenueCLI
from .event_venue_cli import EventVenueCLI

# Optionally, you can define an __all__ list to specify which symbols are exported
__all__ = ['main', 'EventCLI', 'GuestCLI', 'VenueCLI', 'EventVenueCLI']
