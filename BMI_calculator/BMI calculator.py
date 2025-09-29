#BMI calculator using height and weight entered by user and classifying it as underweight, normal, overweight, etc
height = float(input("Enter your \"HEIGHT\" in \"METRES\" or \"CENTIMETRES\" = "))
weight = float(input("Enter your \"WEIGHT\" in \"KILOGRAMS\" = "))

if height and weight <=0:
    print("Sorry, Please enter the correct values!!")
elif height>3:
    print("Look's like you have entered height in \"CENTIMETRES\" converting to metres....")
    height /= 100

BMI = weight / (height**2)
print("Your BMI is : " , BMI)

if BMI<16:
    print("category : Severe underweight")
    print("Health risk : very high")
elif 16<=BMI<=16.9:
    print("category : Moderate underweight")
    print("Health risk : High")
elif 17<=BMI<=18.4:
    print("category : Mild underweight")
    print("Health risk : Elevated")
elif 18.5<=BMI<=24.9:
    print("category : Normal weight")
    print("Health risk : low")
elif 25<=BMI<=29.9:
    print("category : Overweight")
    print("Health risk : Increased")
elif 30<=BMI<=34.9:
    print("category : Obesity Class I")
    print("Health risk : High")
elif 35<=BMI<=39.9:
    print("category : Obesity Class II")
    print("Health risk : Very High")
else:
    print("category : Obesity Class III")
    print("Health risk : Extremely High")