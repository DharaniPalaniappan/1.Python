class age():
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
      
    def SubfieldsInAISubfields():
        subfields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for a in subfields:

            print(a)
            
    def OddEven():
        num = int(input("enter a number :"))
        if((num%2)==0):
            print(num," is Even number")
        else:
            print(num," is Odd number")
            

    def percentage():
        a = int(input("Subject1="))
        b = int(input("Subject2="))
        c = int(input("Subject3="))
        d = int(input("Subject4="))
        e = int(input("Subject5="))
        Total = a+b+c+d+e
        print("Total=",Total)
        Perc = (Total/500)*100
        print("Percentage=",Perc)
    def triangle():
        a = int(input("Height:"))
        b = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area = (a*b)/2
        print("Area of Triangle:",Area)
        H1 = int(input("Height1:"))
        H2 = int(input("Height2:"))
        Br = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter = H1+H2+Br
        print("Perimeter of Triangle:",Perimeter)




  