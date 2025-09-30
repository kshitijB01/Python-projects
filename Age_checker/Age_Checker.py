#Inputting birth year from user and calculating age and checking for some eligibility criterias
from datetime import datetime

Birthyear = int(input("Enter your Birth year: "))
current_year = datetime.now().year
age = current_year - Birthyear
print(f"Your age is {age}")

print("\n✅ Based on your age, here are your eligibilities:")

if 16<=age<=17:
    print("Apply for learner's driver liscence")
    print("Take part-time jobs/internships")
    print("Give some entrance exams")
    print("can choose streams (Science/Commerce/Arts)")

if 18<=age<21:
    print("Eligible to vote")
    print("Eligible to Drive")
    print("Get Passport without parental consent")
    print("Sign legal contracts and open bank accounts")
    print("Apply for PAN-CARD & CREDIT-CARDS")

if 21<=age<25:
    print("Legal age for men to marry in India")
    print("Eligible for UPSC civil services")
    print("Can contest for panchayat/local body elections")
    print("Can adopt a child")

if 25<=age<30:
    print("Eligible to contest Lok sabha elections")
    print("Can contest for Legislative Assembly elections")
    print("Many corporate leadership programs open up")

if 30<=age<35:
    print("Eligible to contest Rajya sabha elections")
    print("Eigible to contest State legislative council elections")

elif age>=35:
    print("Eligible to contest for president or Vice-president of India")