class user:
    def __init__(self, first_name, last_name, age, institution, fav_club):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.institution = institution
        self.fav_club = fav_club
        self.login_attempts = 0
    def describe_user(self):
        print("The name of this user is " + self.first_name + " " + self.last_name +". He is " + str(self.age) + " years old. The name of his institution is " + self.institution + " and his favourite club is " + self.fav_club )
       # print("Your login attempts is "+str(self.login_attempts)+ "times")
    def user_greet(self):
        print("Welcome to Dontezzy Palace.... Thank you for your service.")
    def user_greet1(self):
        print("Welcome to Damtezzy Palace.... Thank you for your service.")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Your login attempts have been reset..... Thanks")
class Admin(user):
    def __init__(self,first_name, last_name, age, institution, fav_club):
        super().__init__(first_name, last_name, age, institution, fav_club)
        self.privilege1 = "Can add post"
        self.privilege2 = "Can delete post"
        self.privilege3 = "Can ban user"
        self.privileges = self.privileges()

    class privileges:
        def __init__(self):
            self.privilege1 = "Can add post"
            self.privilege2 = "Can delete post"
            self.privilege3 = "Can ban user"


        def show_privileges(self):
            print(self.privilege1)
            print(self.privilege2)
            print(self.privilege3)



#my_user = user("Quadri", "Dolapo", 22, "University of Ibadan", "Chelsea")
#ur_user = user("Oyindamola", "Olaitan", 22, "Oke-ogun polytechnic", "realmadrid")

my_user = Admin("Quadri", "Dolapo", 22, "University of Ibadan", "Chelsea")

my_user.describe_user()
my_user.privileges.show_privileges()
#our_user.describe_user()
#my_user.user_greet()
#our_user.user_greet1()
