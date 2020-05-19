class Restaurant():
    """simple attempt to create a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """intialises name and type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(self.restaurant_name + " serves " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print("The restaurant " + self.restaurant_name + " is now open")


restaurant_0 = Restaurant("Chipotle", "Mexican")

print(restaurant_0.restaurant_name)
print(restaurant_0.cuisine_type)
restaurant_0.describe_restaurant()
restaurant_0.open_restaurant()

# testing