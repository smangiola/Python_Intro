name = input("What is your name?") #this is an input for the user to type
print("Hi there, " + name) #it "prints" or shows text in the terminal
#then it concatenates (+) a string with the person's input
print(name + " is a cool person.")
print("Hi " + name + "! Let me make sure you name is " + name + "?")

color = input("What is your favorite color?")
print("You like " + color)
print("I like " + color + " as well. " + color + " is a nice shade.")

email = input("Please enter your email:")
nickname = input("What is your nickname?")
address = input("What is your address?")

age = int(input("Please enter your age: "))

print("Your email is " + email + " and your nickname is " + nickname + "." + "You live in " + address + " and you are " + str(age) + " years old.")