responses = {}
polling_active = True

while polling_active:
    name = input("What is your name: ")
    mountain = input("Which mountain would you like to climb someday: ")
    responses[name] = mountain
    print(f"{name} want to climb {mountain}")

    repeat = input("Would you like to let another person respond (yes/no): ")
    if repeat.lower() == 'no':
        polling_active = False

print(responses)