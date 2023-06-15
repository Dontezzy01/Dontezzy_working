class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 120

    def describe_restaurant(self):
        print("The restaurant name is " + self.restaurant_name + ".")
        print(str(self.cuisine_type) + " is the cuisine type")
        print(str(self.number_served) + " have been served in the restaurant.")

    def open_restaurant(self):
        print("The restuarant is Open")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


class IceScreamStand(restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.chocolate = "chocolate"
        self.strawberry = "strawberry"
        self.vanila = "vanila"

    def display_flavors(self):
        print("The list of flavors available are: " + self.chocolate + ", "+ self.strawberry + " and " + self.vanila)



my_restaurant = IceScreamStand("Dontezzy", 24)
my_restaurant.describe_restaurant()
print(my_restaurant.display_flavors())


