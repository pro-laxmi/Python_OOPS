class student:
    def __init__(self, name, mark):
        self.name=name
        self.mark=mark
    def average(self):
        sum=0
        for val in self.mark:
            sum+=val
        avg=sum/len(self.mark)
        return avg
Dec="y"
list=[]
while True:
    if Dec=="y":
        a=int(input("Enter the marks:-"))
        list.append(a)
        Dec=input("If you want to enter another mark (y/n):-")
    elif Dec=="n":
        break
    else:
        print("OOPS! you have entered wrong input....")
        break
s1=student("Lala",list)
print("Your average marks is",round(s1.average(),2))