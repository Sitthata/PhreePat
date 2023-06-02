import random

random_question = input("Ask me something: ")

i = random.randint(1,5)
if i == 1:
    print("Yes")
elif i == 2:
    print("No")
elif i == 3:
    print("Maybe")
elif i == 4:
    print("Yes definitely")
else:
    print("My source say no")