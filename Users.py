class User():
    """A simple attempt to model a computer user."""

    def __init__(self, first_name, last_name, Screen_name):
        """Initialize name and age attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.Screen_name = Screen_name


    def describe_user(self):
        """describes the attributes of a user"""
        print(self.first_name + "\n" + self.last_name + "\n" + self.Screen_name)

    def greet_user(self):
        """Prints a personalzed greeting to user"""
        print("Greatings "+ self.first_name + " " + self.last_name +", welcome to the matrix.")

My_User = User("Douglas", "Tucker", "Gusgus")

My_User.greet_user()
My_User.describe_user()

