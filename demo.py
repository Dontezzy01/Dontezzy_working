from sharp import*
def func1():
    add()
    print("From func 1")
def func2():
    sub()
    print("from func 2")
def func3():
    print("From func 3")
def main():
    func1()
    func2()
    func3()
main()

filename= "programming.txt"
with open(filename, "a") as file_object:
    pass
    #file_object.write("I love creating good app environment.\n")
    #file_object.write("I love being backbone of backend fields.\n")

filename = "Guest.txt"
with open(filename, "w") as file_object:
    result = file_object.write(str(input("Enter your fullname: \n")))
    for data in result:
        print("Good day.... Thanks")
   # result1= file_object.write(str(input("What are your hobbies: \n")))


















#from sharp import*
#a = 9
#b = 3
#c = muilti(a,b)
#print(c)


#def main():
 #   print("Hello")
  #  print("Welcome user!")
#if __name__ == "__main__":
    #main()