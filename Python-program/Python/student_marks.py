Hindi = int(input("please enter your hindi marks: "))
Math = int(input("please enter your math marks: "))
English = int(input("please enter your english marks: "))
Science = int(input("please enter your science marks: "))

total = Hindi + Math + English + Science
percentage = (total / 4)

print("\nTotal marks: ",total)
print("percentage: ", percentage)

if percentage>=60:
    print("First Division")

else:
    print("failed")