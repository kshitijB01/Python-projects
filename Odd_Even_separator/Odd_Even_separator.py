#inputting a list from user and separating odd and even numbers

numbers = list(map(int, input("Enter the numbers by giving spaces: ").split()))

even_numbers = []
odd_numbers = [] 

for x in numbers:
    if x % 2 == 0:
        even_numbers.append(x)
    else:
        odd_numbers.append(x)

print("Even numbers are:",even_numbers)
print("Odd numbers are:",odd_numbers)