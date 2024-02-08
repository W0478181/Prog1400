class Person:
    def __init__(self,first_name,last_name,mobile,email):
        self.first_name = first_name
        self.last_name = last_name
        self.mobile = mobile
        self.email = email
    def make_trip(self,route):
        print(f'{self.first_name,self.last_name} is making a trip along the route: {route}')
 
class Driver(Person):
    def __init__(self, first_name, last_name, mobile, email, v_make, v_model):
        super().__init__(first_name, last_name, mobile, email)
        self.v_make = v_make
        self.v_model = v_model