# year= int(input("Enter the yea...."))
# if year % 4 ==0:
#     print("yes")
# else:
#     print("not")
# if year%100 == 0:
#     print("not")
# else:
#     print("yes")
# if year % 400 == 0:
#     print('yes')
# else:
#     print('no')




year =int(input("enter the year........."))
if year % 4 ==0 :
    if year % 100 != 0:
        print("not leap year")
    elif year % 400 ==0:
        print("leap year")



else:
    print("Not")