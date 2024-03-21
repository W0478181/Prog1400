class Person:
    def __init__(self, first_name, last_name, mobile, email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email

    def make_trip(self, route):
        print(f"{self.first_name} {self.last_name} is making a trip to {route.destination}.\n{self.first_name} will leave from {route.origin} and stop at {route.stop}.")

class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email, v_make, v_model, v_color, v_type):
        super().__init__(first_name, last_name, mobile, email)
        self.v_make = v_make
        self.v_model = v_model
        self.v_color = v_color
        self.v_type = v_type
    
    def make_trip(self, route):
        super().make_trip(route)
        print(f"{self.first_name} {self.last_name} is driving a {self.v_color} {self.v_make} {self.v_model} {self.v_type}.")

class Rider(Person):
    def __init__(self, first_name, last_name, mobile, email):
        super().__init__(first_name, last_name, mobile, email)

    def make_trip(self, route, driver):
        print(f"{self.first_name} {self.last_name} is requesting a ride to {route.destination}.\n{self.first_name} is availible to meet at {route.stop}.")
        print(f"{self.first_name} {self.last_name}, {driver.first_name} {driver.last_name} will pick you up at {route.stop}.")

class Route:
    def __init__(self, origin, stop, destination):
        self.origin = origin
        self.stop = stop
        self.destination = destination


driver1 = Driver("Dyan", "Bryan", "902-420-6969", "Dbryan@yahoo.com", "Nissan", "Sentra", "Black", "car")
rider1 = Rider("Paul", "Blart", "902-123-4567", "PB@yahoo.com")
route = Route("Antigonish", "Bayside", "Strait Area")

driver1.make_trip(route)
rider1.make_trip(route, driver1)