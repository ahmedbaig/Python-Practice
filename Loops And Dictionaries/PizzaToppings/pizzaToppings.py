print("\n----Ahmed's pizza palace----\n\n")

customer = []
while True:
    newCustomer = input('\n\nMake New Customer? ')
    if newCustomer == 'y' or newCustomer == 'yes':

        customerName = input('Enter customer name: ')
        crustType = input('Enter crust type: ')
        toppings = input('Would you like topping on that pizza? ')
        topping = 'no extra toppings'

        if toppings == 'yes' or toppings == 'y':
            topping = []
            howMany = int(input('how many toppings? '))
            total = howMany
            while howMany != 0:
                topping.append(input('Enter topping ' + str(total-howMany+1) + ": "))
                howMany -= 1
                if howMany == 0:
                    response = input('Do you want to add more toppings? ')
                    if response == 'y' or response == 'yes':
                        howMany = int(input('how many more toppings? '))
                        total += howMany
        elif toppings == 'no' or toppings == 'n':
            topping = 'no extra toppings'
        order = {
            'name': customerName,
            'crust': crustType,
            'topping': topping
        }
        customer.append(order)
    elif newCustomer == 'n' or newCustomer == 'no':
        print('\n\n----List of Customers----\n\n')
        for order in customer:
            print('Customer Name: ' + order['name'].title())
            print("\nCrust Type: " + order['crust'])
            print("\nNumber of toppings: " + str(len(order['topping'])))
            incri = 1
            for top in order['topping']:
                print("\n - Topping "+str(incri)+": " + top)
                incri += 1