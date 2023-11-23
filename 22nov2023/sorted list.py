#17. Merge two sorted lists into a single sorted list.
list1=[2,4,3,5,1,7]
list2=[5,3,2,8,8,2]
list1.sort()
list2.sort()
list3=list1+list2
list3.sort()
print(list3)
