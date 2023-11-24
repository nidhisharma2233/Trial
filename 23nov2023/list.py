
"""1. Advanced Data Structures:
   - In-depth exploration of lists, sets, and dictionaries.
   - Advanced operations and methods on these data structures.
   - Use cases and practical applications for each data structure."""

list1=[10,20,3,40,"ankit","fall","ankit"]

#list allow dublicate value
print(list1," ",type(list1)," ",len(list1))

#list indexing
print(list1[2::-1]," ",list1[2:6])

#list count method
print("count method=",list1.count("ankit"))

#change list elemnets
list1[1] = "blackcurrant"
print("change element=",list1)

#insert function,append function(it add the element in the last position)
list1.insert(2, "watermelon")
list1.append("orange")
print("after indexing=",list1)

#remove list items
list1.remove("blackcurrant")
list1.pop()
list1.pop(1)
print("after remove=",list1)

#list comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
list2 = [x for x in fruits if "a" in x]
print("list comprehension=",list2)

#sort and sorted
fruits.sort(reverse = True)
print("after sort=",fruits)
s=sorted(fruits)
print("sorted fun=",s)

#Make a copy of a list with the copy() method
onelist = ["apple", "banana", "cherry"]
mylist = onelist.copy()
print(mylist)


































