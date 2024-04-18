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





# first_restaurant = Restaurant('Clode Mone', 'franc')
#
# print(first_restaurant.restaurant_name)
# print(first_restaurant.cuisine_type)
# first_restaurant.discribe_restaurena()
# first_restaurant.open_restaurant()
#
# second_restoran = Restaurant('kedr', 'luver')
#
# second_restoran.discribe_restaurena()
#
# restaurant = Restaurant('Chaihana', 'grus')
# print('///////////////////////////////////////////////////////////////////////////////')
# print(restaurant.number_served)
# restaurant.number_served = 25
# print(restaurant.number_served)
#
# restaurant.set_number_served(99)
#
# print(restaurant.number_served)
#
# restaurant.increment_number_served(20)
#
# print(restaurant.number_served)


