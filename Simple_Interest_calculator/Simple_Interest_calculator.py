#Calculating Simple Interest 

P = float(input("Enter the principle amount (₹) : "))
R = float(input("Enter the annual interest rate (%) : "))
T = float(input("Enter the time duration (years) : "))

SI = (P * R * T)/100
print(f"The Simple Interest on ₹{P:.2f} at {R:.2f} % for {T:.2f} years is: ₹{SI:.2f}")