#Problem 1: Association
class Driver:
    def __init__(self, name):
        self.name = name

class Car:
    def __init__(self, driver):
        self.driver = driver

#Problem 2: Aggregation
class Employee:
    def __init__(self, name):
        self.name = name

class Company:
    def __init__(self, employees):
        self.employees = employees

#Problem 3: Composition
class Engine:
    def __init__(self):
        print("Engine created")

class Car:
    def __init__(self):
        self.engine = Engine()