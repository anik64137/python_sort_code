import random

inp=input("enter your seed")
random.seed(inp)

num = int(random.randint(1,2))

if num ==1:
    print("head")
else:
    print("tell")