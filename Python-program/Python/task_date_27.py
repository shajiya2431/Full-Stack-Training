hindi = int(input("please enter your hindi marks: "))
english = int(input("please enter your english marks: "))
math = int(input("please enter your math marks: "))
science = int(input("please enter your science marks: "))

total = hindi + english + math + science
percentage = (total / 4)

print("\nTotal marks: ",total)
print("percentage: ",percentage)


if percentage >= 60:
    print("Grade: A")

elif percentage >= 45:
    print("Grade: B")

elif percentage >= 33:
    print("Grade: C")

else:
    print("Result: Failed")
