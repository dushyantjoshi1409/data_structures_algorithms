class Car():
    def __init__(self, name, model, color, year):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
        self.start()
    def start(self):
        print(f"{self.name} started in {self.year}")

ola = Car("Ola", "S1", "Red", 2020)