responses = {}

polling_active = True

while polling_active:
    name = input("Enter your name: ")
    response = input("Are you going for school tomorrow: ")

    responses[name] = response

    repeat = input("Add any other person response?")

    if repeat == 'no':
        polling_active = False
    elif repeat == 'n':
        polling_active = False

print('\n\n ----polling results----\n\n')

for name, response in responses.items():
    print(name + " will " + response + " go to school")