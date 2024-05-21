name_one=input("Enter the first name......").lower()
name_two=input("Enter the 2nd name......").lower()

print(name_one,name_two)

r=name_one.count("r")
u=name_one.count("u")
e=name_one.count("e")
l=name_one.count("l")

r2=name_two.count("r")
u2=name_two.count("u")
e2=name_two.count("e")
l2=name_two.count("l")

print(u,r)

#true
true=r*1+u*2+e*2+l*1
love=r2*1+u2*2+e2*2+l2*1

true_srt=str(true)
love_srt=str(love)
valu= true_srt+love_srt
valu2=int(valu)
print(valu2)




# T occurs 0 times
#
# R occurs 1 time
#
# U occurs 2 times
#
# E occurs 2 times
#
# Total = 5
#
# L occurs 1 time
#
# O occurs 0 times
#
# V occurs 0 times
#
# E occurs 2 times

