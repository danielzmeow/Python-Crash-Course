# use input() to get user input contents
message = input("Just input your name: ")
print(f"Hello, {message}!")

# use int() to transfer input string into integer
age = int(input("Just input your age: "))
int_age = int(age)
if int_age >= 18:
    print("Welcome!")
else:
    print("You are too young to enter!")

# prompt defined exit
prompt = "\nTell me something, and I will repeat it back to you "
prompt += "(Enter 'quit' to end the program.): "

message = ""
while message != 'quit':
    message = input(prompt)
if message != 'quit':
    print(f"\n{message}")