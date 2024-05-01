import random

randomNum = random.randrange(1, 10)

print(randomNum)

typeCastingOfRandomNum = complex(randomNum)

print(typeCastingOfRandomNum)  # complex number formation

typeCastingOfRandomNum = float(randomNum)

print(typeCastingOfRandomNum)

fruit = "banana"

# print(fruit[1])  # String like an array

for x in fruit:
    print(x)
# loop in String be like
"""
b
a
n
a
n
a
"""
print(len(fruit))

print("ba" in fruit)  # true
