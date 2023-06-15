class user:
    def __init__(self, first_name, last_name, age, institution, fav_club):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.institution = institution
        self.fav_club = fav_club
        self.login_attempts = 0
    def describe_user(self):
        print("The name of this user is " + self.first_name + " " + self.last_name +". He is " + str(self.age) + " years old. The name of the institution is " + self.institution + " and his/her favourite club is " + self.fav_club )
        print("Your login attempts is "+str(self.login_attempts)+ "times")
    def user_greet(self):
        print("Welcome to Dontezzy Palace.... Thank you for your service.")
    def user_greet1(self):
        print("Welcome to Damtezzy Palace.... Thank you for your service.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Your login attempts have been reset..... Thanks")



my_user = user("Quadri", "Dolapo", 22, "University of Ibadan", "Chelsea")
our_user = user("Oyindamola", "Olaitan", 22, "Oke-ogun polytechnic", "realmadrid")
my_user.describe_user()
#our_user.describe_user()
#my_user.user_greet()
#our_user.user_greet1()
my_user.increment_login_attempts()
my_user.describe_user()

my_user.increment_login_attempts()
my_user.describe_user()

my_user.increment_login_attempts()
my_user.describe_user()

my_user.reset_login_attempts()

my_user.increment_login_attempts()
my_user.describe_user()
