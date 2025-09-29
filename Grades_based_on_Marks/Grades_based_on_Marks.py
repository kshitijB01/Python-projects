#inputing marks from user and giving the grades
phy = float(input("Enter the marks of phyics out of 100: "))
chem = float(input("Enter the marks of Chemistry out of 100: "))
maths = float(input("Enter the marks of Mathematics out of 100: "))
Total = phy + chem + maths

if 91<=phy<=100:
    print("You Got A Grade in PHYSICS!")
elif 81<=phy<=90:
    print("You Got B Grade in PHYSICS!")
elif 71<=phy<=80:
    print("You Got C Grade in PHYSICS!")
else:
    print("You Got D Grade in PHYSICS!")

if 91<=chem<=100:
    print("You Got A Grade in CHEMISTRY!")
elif 81<=chem<=90:
    print("You Got B Grade in CHEMISTRY!")
elif 71<=chem<=80:
    print("You Got C Grade in CHEMISTRY!")
else:
    print("You Got D Grade in CHEMISTRY!")

if 91<=maths<=100:
    print("You Got A Grade in MATHEMATICS!")
elif 81<=maths<=90:
    print("You Got B Grade in MATHEMATICS!")
elif 71<=maths<=80:
    print("You Got C Grade in MATHEMATICS!")
else:
    print("You Got D Grade in MATHEMATICS!")

if 291<=Total<=300:
    print("Your Grand Total is A Grade")
elif 281<=Total<=290:
    print("Your Grand Total is B Grade")
elif 271<=Total<=280:
    print("Your Grand Total is C Grade")
else:
    print("Your Grand Total is D Grade")