marks = {}

English= input("My English Marks: ")
Hindi = input("My Hindi Marks: ")
Urdu = input("My Urdu Marks: ")
Math = input("My Math Marks: ")
Science = input("My Science Marks: ")

marks["English"] =int(English)
marks["Hindi"] =int(Hindi)
marks["Urdu"] = int(Urdu)
marks["Math"] =int(Math)
marks["Science"] =int(Science)


total = marks["English"]+marks["Hindi"]+marks["Urdu"]+marks["Math"]+marks["Science"]
percentage = total / 5

print("Result")
print("total Marks: ",total)
print("percentage: ", percentage, "%")


