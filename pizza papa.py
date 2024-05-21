print("welcome to our pizza papa!")
size=input("enter what would you like to oder S M M.........")
pepproni=input("if you want then type Y or N>>>>>>>>>>>")
chesse=input("if you want chesse then Y else N///////////")

bill=0
if size == "S":
    bill+=15
elif size == "M":
    bill+=20
elif size == "L":
    bill += 25

if pepproni =="Y":
    if size == ("S"):
        bill+=2
    else:
        bill +=3

if chesse=="y":
    bill +=1

print(f"your final bill is {bill}")
