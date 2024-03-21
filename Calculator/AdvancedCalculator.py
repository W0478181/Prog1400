# Define a class for Advanced Caluclations
# The @staticmethod decorator is used to define a method within a class
# that does not access or modify the class or instance state.
# This means that the method does not have access to the instance (self)
# or the class (cls) and behaves like a regular function outside the class.
# When you define a method within a class, by default it is an instance method,
# meaning it operates on an instance of the class and has access to the instance
# attributes via the self parameter. However, sometimes you may want to define a
# method that does not require access to the instance or the class itself.
class Calculator:
#Define functions for basic arithemic operations
    @staticmethod
    def exponentiate(base, exponent):
        return base ** exponent

    def add(x,y):
        return x + y

    def sub(x,y):
        return x - y

    def mult(x,y):
        return x * y

    def div(x,y):
        if y == 0:
            raise ValueError("Cannot divide by 0")
        return x / y

    def expo(base, exponent):
        return base ** exponent
