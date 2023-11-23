#7. Perform basic arithmetic operations (addition, subtraction, multiplication, division) using user input
a=int(input("enter num"))
b=int(input("enter 2nd num"))
c=input("enter choice 1=add 2=sub 3=multi 4=div")

if c=="add":
    d=a+b
    print("add=",d)
if c=="sub":
    d=a-b
    print("sub=",d)
if c=="multi":
    d=a*b
    print("multi=",d)
if c=="div":
    d=a/b
    print("div=",d)

else:
    print("wrong choice")
