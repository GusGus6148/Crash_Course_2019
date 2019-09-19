sandwich_orders = ['pastrami', 'salami', 'meatball','pastrami', 'philly cheese', 'veggie','pastrami', 'tuna']

finished_sandwiches = []

print("\nI'm sorry the deli has run out of pastrami for the day\n")

while sandwich_orders:
    order = sandwich_orders.pop()
    if order != 'pastrami':
        print("I made your " + order + " sandwich.")
        finished_sandwiches.append(order)
    else:
        continue

print("\nI have made the following sandwiches")

for sandwhich in finished_sandwiches:
    print("-" + sandwhich)


