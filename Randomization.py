import random
#
# toss = random.choice(["Head", "Tail"])
#
# print(toss)
# capitalize() method capitalizes the first character of a string
# split() method splits a list separated by mentioned character
names = input("Enter the names separated by a comma (,): ").split(",")

# print(names)

titled_names = [i.title() for i in names]

print(titled_names)

bill_payer = random.choice(titled_names)

print(bill_payer + " will pay the bill.")
