def make_sandwich(*toppings):
    print("\nMaking a sandwhich with the following toppings:")
    for topping in toppings:
        print("-" + topping)


make_sandwich('Salami', 'cheese')
make_sandwich('bacon', 'lettuce', 'tomato')
make_sandwich('cheese')
