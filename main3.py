height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight//height**2)

print(bmi)

if bmi  <=18.5 :
    print("you are underweight")
elif bmi <=25  :
    print("you are normal weight")
elif bmi <=30 :
    print("you are overweight")
elif bmi <= 35:
    print("you are obese")
else:
    print("you are clinically obese.")