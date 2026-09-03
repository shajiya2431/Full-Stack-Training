Student_details1={
    "id":input("please enter student iD: "),
    "name":input("please enter your name: "),
    "address":input("please enter your Address: ")

}

Student_details2={
    "id":input("\nplease enter student iD: "),
    "name":input("please enter your name: "),
    "address":input("please enter your Address: ")
}


print("\nStudent details 1")
print("student id:",Student_details1["id"].zfill(18))
print("student name: ",Student_details1["name"].isalpha())
print("student address: ",Student_details1["address"].isalpha())

print("\nStudent details 1")
print("student id:",Student_details2["id"].zfill(18))
print("student name: ",Student_details2["name"].isalpha())
print("student address: ",Student_details2["address"].isalpha())