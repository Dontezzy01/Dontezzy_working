class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 120
    def describe_restaurant(self):
        print("The restaurant name is "+self.restaurant_name+".")
        print(str(self.cuisine_type) +" is the cuisine type")
        print( str(self.number_served) + " has been served in the restaurant.")
    def open_restaurant(self):
        print("The restuarant is Open")
    def set_number_served(self, number):
        self.number_served = number
    def increment_number_served(self,number):
        self.number_served += number

my_restaurant = restaurant("Dontezzy", 24)
our_restaurant = restaurant("Damtezzy", 7)
your_restaurant = restaurant("Tezzy", 20)

#print(my_restaurant.restaurant_name)
#print(my_restaurant.cuisine_type)

my_restaurant.set_number_served(129)
my_restaurant.describe_restaurant()
my_restaurant.increment_number_served(20)
my_restaurant.describe_restaurant()

#our_restaurant.describe_restaurant()
#your_restaurant.describe_restaurant()
my_restaurant.open_restaurant()