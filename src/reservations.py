from enum import Enum

# Define an Enum for seat types
class SeatType(Enum):
    SITTING_DESK_MONITOR = "sitting desk with monitor"
    STANDING_DESK_MONITOR = "standing desk with monitor"
    COMMUNITY_SEAT = "community seat"

class Reservations:
    def __init__(self):
        # Initialize an empty list to store current reservations
        self.current_reservations = []

        # Add default reservations
        self.check_in("Alice", SeatType.SITTING_DESK_MONITOR)
        self.check_in("Alice", SeatType.SITTING_DESK_MONITOR)
        self.check_in("Bob", SeatType.STANDING_DESK_MONITOR)
        self.check_in("Charlie", SeatType.COMMUNITY_SEAT)
        self.check_out("Alice")

    # Method to check students in (add a reservation)
    def check_in(self, name, seat_type):
        # Create a dictionary for the student's reservation (store the SeatType enum)
        reservation = {'name': name, 'seat_type': seat_type}
        # Add the reservation to the list
        self.current_reservations.append(reservation)
        print(f"Checked in: {name} with seat type: {seat_type.value}")

    # Method to check students out (remove a reservation)
    def check_out(self, name):
        # Find and remove the reservation by name
        for reservation in self.current_reservations:
            if reservation['name'] == name:
                self.current_reservations.remove(reservation)
                print(f"Checked out: {name}")
                return
        print(f"No reservation found for {name}")

    # Method to get the current reservations list with formatted output
    def get_reservations(self):
        if not self.current_reservations:
            return "No current reservations."
        
        # Create a list of formatted strings for each reservation
        formatted_reservations = []
        for reservation in self.current_reservations:
            # Access the SeatType enum and use its value attribute
            formatted_reservations.append(f"Name: {reservation['name']}, Seat Type: {reservation['seat_type'].value}")
        
        # Join the formatted strings with a newline character
        return "\n".join(formatted_reservations)

# Example usage
todays_reservations = Reservations()

# Print the current reservations to see the default values
print() # blank line for visual purposes in console
print("Current reservations:")
print(todays_reservations.get_reservations())