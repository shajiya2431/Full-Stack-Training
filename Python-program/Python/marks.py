name = input ("Enter student name: ")

Hindi = int(input("Enter Hindi Marks: "))
English = int(input("Enter English Marks: "))
Math = int(input("Enter Math Marks: "))
Science = int(input("Enter Science Marks: "))
Computer = int(input("Enter Computer Marks: "))

total = Hindi + English + Math + Science + Computer 
percentage = total / 5

print("Result")
print("Name:", name)
print("total Marks: ",total)
print("percentage: ", percentage, "%")