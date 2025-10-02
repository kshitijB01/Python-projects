#Inputting marks of student from user and calculating percentage, average, highest, lowest, and count of passing students.
import math
totmarks = list(map(int, input("Enter the total marks(out of 500) according to Roll-numbers by giving spaces: ").split()))

task = input("Enter the task you want to perform like calculating (average / highest / lowest / count of passing students): ")

total = 0
largest = -math.inf
smallest = math.inf
count = 0
if task == "average":
    for x in totmarks:
        total = total + x
        x+1

    avg = total/len(totmarks)
    print("Average of total marks is:",avg) 

elif task == "highest":
    for x in totmarks:
        if largest < x:
            largest = x
        else:
            -1
    print("highest total marks scored are:",largest)

elif task == "lowest":
    for x in totmarks:
        if smallest > x:
            smallest = x
        else:
            -1
    print("lowest total marks scored are:",smallest)

elif task == "count":
    for x in totmarks:
        if x >= 175:
            count+=1

    print("Number of passed students are:",count)






