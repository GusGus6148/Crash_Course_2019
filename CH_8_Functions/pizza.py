def make_pizza(size, *toppings):
    """Summarize the pizza we area about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the foloowing toppings:")
    for topping in toppings:
        print("- " + topping)


