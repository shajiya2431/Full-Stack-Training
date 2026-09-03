import datetime

number = int(input("plase enter create a  file: "))
if 1<=number<=20:
        time_stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        for i in range(1,number+1):
            with open(f"shajiya_{time_stamp}_{i}.txt","w") as file:
                file.write(f"i am from bihar{i}")

            with open(f"shajiya{i}.txt","r") as file:
                data=file.read()
            print(data)
         

    
else:
    print("please enter number (1 to 20)")
