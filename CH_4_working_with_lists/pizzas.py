pizzas = ['pepperoni', "hell's canyon", 'green olives']

for pizza in pizzas:
    print("I like " + pizza + " pizza.")

print("\nI like pizza so much!")

friends_pizza = pizzas[:]

pizzas.append('jalepeno')
friends_pizza.append('dessert')

print("\nMy favorite pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are: ")
for pizza in friends_pizza:
    print(pizza)