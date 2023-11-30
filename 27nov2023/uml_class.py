class nidhi:
    def __init__(self,name,age,Address,Qualification):
        self.name=name
        self.age=age
        self.Address=Address
        self.Qualification=Qualification

    def Your_Name(self):
        return self.name
    def Your_age(self):
        return self.age
    def Your_DOB(self):
        return self.Address
    def Your_Qualification(self):
        return self.Qualification
print("-----Fill the your Details---")
a=input("Ether the Your Name:")
b=int(input("Enter the Your Age:"))
c=input("Enter the Your Address:")
d=input("Enter the Your Qualification:")
obj=nidhi(a,b,c,d)
print()
print("---your Details---")
print("Your Name:",obj.Your_Name())
print("YOur Age:",obj.Your_age())
print("Your Address:",obj.Your_DOB())
print("YOur Qualification:",obj.Your_Qualification())