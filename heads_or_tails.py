import random

value = random.random()
round_value = round(value)

print(round_value)

if round_value == 1:
    print("Heads")
else:
    print("Tails")