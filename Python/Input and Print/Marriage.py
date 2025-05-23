class age():
    def agecal():
        age = int(input("Enter you age"))
        if(age<18):
           print("childrens")
           message = "Children"
        elif(age<50):
           print("Adults",)
           message = "Adult"
        else:
           print("Seniors")
           message = "Senior"
        return message
    def Eligible():
        Gender = input("Enter a Gender :")
        Age = int(input("Enter a Age :"))
        if(Gender == "Male" or Gender == "M"):
            if(Age >=21):
                print("Eligible")
            else:
                print("Not eligible")
        elif(Gender=="Female" or Gender == "F"):
            if(Age>=18):
                print("Eligible")
            else:
                print("Not eligible")

  
