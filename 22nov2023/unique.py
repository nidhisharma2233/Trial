
#16. Check if all elements in a list are unique.
list1=[1,2,3,4]
count = 0
for i in list1:

    for k in list1:
        if i==k:
            count+=1
if count==4:
    print("all elements are unique")
else:
    print("all elements are not unique")