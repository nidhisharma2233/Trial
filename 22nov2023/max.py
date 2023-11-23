#11. Find the maximum and minimum values in a list of numbers.
a=[5,2,3,4,5,6,3]
for i in a:
    for k in a:
        if k>i:
            b=k
        if k<i:
           c=k
print("max=",b)
print("min=",c)