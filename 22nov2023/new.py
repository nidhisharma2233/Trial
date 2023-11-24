list1=[1,2,3,4,5]
list2=[2,3,4,5,6]
dict1={}
for i in range(len(list1)):
    dict1[list1[i]]=list2[i]
print(dict1)
