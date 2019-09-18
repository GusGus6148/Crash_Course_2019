
amount = 5

while amount <= 10:
    question = input("do you want to stop y/n ")
    if question == "y":
        break
    else:
        amount = amount + 1
    print(amount)