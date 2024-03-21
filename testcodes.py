from datetime import datetime

class Person:
    def __init__(self, first_name, last_name, age, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.mobile = mobile
        self.email = email
    
    def details(self):
        return f"Details\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nContact: {self.mobile}, {self.email}"
    
    def make_trip(self, route):
        print(f"{self.first_name} {self.last_name} is making a trip to {route.destination}.\n{self.first_name} will leave from {route.origin} and stop at {route.stop}.")

    
class Driver(Person):
    def __init__(self, first_name, last_name, age, mobile, email, v_make, v_model, v_color, v_type, plate):
        super().__init__(first_name, last_name, age, mobile, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_color = v_color
        self.v_type = v_type
        self.plate = plate

    def details(self):
        return f"Driver {super().details()}"    
    
    def make_trip(self, route):
        super().make_trip(route)
        print(f"{self.first_name} {self.last_name} is driving a {self.v_color} {self.v_make} {self.v_model} {self.v_type}.")
    
class Rider(Person):
    def __init__(self, first_name, last_name, age, mobile, email):
        super().__init__(first_name, last_name, age, mobile, email)

    def details(self):
        return f"\nRider {super().details()}"
    
    def make_trip(self, route, driver):
        print(f"{self.first_name} {self.last_name} is requesting a ride to {route.destination}.\n{self.first_name} is availible to meet at {route.stop}.")
        print(f"{self.first_name} {self.last_name}, {driver.first_name} {driver.last_name} will pick you up at {route.stop}.")
    
class Route:
    def __init__(self, origin, stop, destination):
        self.origin = origin
        self.stop = stop
        self.destination = destination

    def details(self):
        return f"\nTrip Details\nOrigin: {self.origin}, Stops: {self.stop}, Destination {self.destination}"
    
class Trip(Route):
    def __init__(self, origin, stop, destination, leave_time, stop_time, end_stop_time, arrival_time):
        super().__init__(origin, stop, destination)
        self.leave_time = leave_time
        self.stop_time = stop_time
        self.end_stop_time = end_stop_time
        self.arrival_time = arrival_time

    def details(self):
        return f"{super().details()},\nLeaving Time: {self.leave_time}, Stopped At: {self.stop_time} Until:{self.end_stop_time} Arrival Time: {self.arrival_time}"
    
def run():
    driver1 = Driver("Aiden","Connolly","19","123-456-7890","asdg@gmail.com","Nissan","Sentra","Black","car","B1T5Y3")
    rider1 = Rider("Dyan","Bryan","37","987-654-3210","cig@gmail.com")
    trip = Trip("St.Andrews","Bayside","Campus",datetime(2024,2,15,7,30),datetime(2024,2,15,7,45),datetime(2024,2,15,8,00),datetime(2024,2,15,8,30))

    journey1 = [driver1, rider1, trip]

    for i in journey1:
        print(i.details())
        i.make_trip(trip)

if __name__ == "__main__":
    run()
