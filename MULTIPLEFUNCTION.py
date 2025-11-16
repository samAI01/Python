class multifunctions():
    def sub_fields():
        print("Machine Learning")
        message="Machine Learning"
        print("Neural Network")
        message="Neural Network"
        print("Vission")
        message="Vission"
        print("Robotics")
        message="Robotics"
        print("Speech processing")
        message="Speech processing"
        print("Natural Learning")
        message="Natural Learning"
        return
    def OddEven():
        a=int(input("Enter the number:"))
        if (a%2==1):
            print(a,"Number is odd")
        else:
            print(a,"Number is even")
            return 
    def MarraigeEligible():
        gender=(input("Enter your gender"))
        print(type(gender))
        age=int(input("Enter your age"))
        print(type(age))
        if (age>=18):
            print("Eligible for a marriage")
            message="Eligible for a marriage"
        elif (age>=21):
            print("Eligible for a marriage")
            message="Eligible for a marriage"
        else:
            print("Not eligible for marriage")
            message="Not eligible for a marriage"
        return message
    def Percentage():
         subject1=int(input("Enter the mark1"))
         subject2=int(input("Enter the mark2"))
         subject3=int(input("Enter the mark3"))
         subject4=int(input("Enter the mark4"))
         subject5=int(input("Enter the mark5"))
         Total=(subject1+subject2+subject3+subject4+subject5)
         print("Total:",Total)
         percentage=Total/5
         print("PERCENTAGE:",percentage)
         return percentage
    def Triangle():
        height=float(input("Enter the height of triangle:"))
        breadth=float(input("Enter the breadth of triangle:"))
        area=(height*breadth)/2
        print("Area of triangle is:",area)
        return area
    def Perimeter():
        height1=float(input("Enter the height of triangle:"))
        height2=float(input("Enter the height of triangle:"))
        breadth=float(input("Enter the breadth of triangle:"))
        perimeter=height1+height2+breadth
        print("Area of triangle is:",perimeter)
        return perimeter