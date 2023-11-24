#set
set1={"one","two",4,6}
print(set1," ",type(set1)," ",len(set1))

#access set items
for x in set1:
  print(x)

#add in set
set1.add("orange")
print(set1)
tropical = {"pineapple", "mango", "papaya"}
set1.update(tropical)
print("after add=",set1)

#remove
set1.remove("one")
set1.pop()
print("after remove=",set1)

#add two set
set2 = {1, 2, 3}

set3 = set1.union(set2)
print("after add=",set3)#use update fun also

#check if all element in set
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

#difference
a= {"apple", "banana", "cherry"}
b= {"google", "microsoft", "apple"}
c = a.difference(b)

print(c)

#intersection
common=x.intersection(y)
print(common)

#disjoint
dis= x.isdisjoint(y)#both sets have different elements
print("disjoint element=",dis)
