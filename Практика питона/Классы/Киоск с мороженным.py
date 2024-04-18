class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def open_restaurant(self):
        print(f"Restaurant {self.restaurant_name.title()} is open")

    def discribe_restaurena(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type.title())

    def set_number_served(self, set_server):
        self.number_served = set_server

    def increment_number_served(self,incremet_sercver):
        self.number_served+=incremet_sercver


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type, flovors):
        super().__init__(restaurant_name, cuisine_type)
        self.flovors = flovors

    def flovors_list(self):
        print(self.flovors)

first_IceCreamStend = IceCreamStand('byby', 'cream', ['red', 'orange', 'yellow'])

first_IceCreamStend.flovors_list()
