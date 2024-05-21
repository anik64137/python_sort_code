name1=input("enter the first name")
name2=input("enter the 2nd name")

combined_names = name1 + name2
lower_names = combined_names.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e



valu=str(first_digit) + str(second_digit)
valu2=int(valu)
print(valu2)

if valu2 < 10 or valu2 >90:
    print(f"Your score is {valu2}, you go together like coke and mentos.")
elif valu2 >=40 and valu2 <=50:
    print(f"Your score is{valu2}, you are alright together.")
else:
    print(f"Your score is {valu2}")