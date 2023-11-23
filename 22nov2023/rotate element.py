#18. Rotate elements in a list by a specified number of positions.
list_1 = [11, 34, 26, 57, 92]
print (" Primary list : " + str(list_1))
list_1 = list_1[3:] + list_1[:3]
print ("Output of the list after left rotate by 3 : " + str(list_1))
list_1 = list_1[-3:] + list_1[:-3]
print ("Output of the list after right rotate by 3(back to Primary list) : "+str(list_1))
list_1 = list_1[-2:] + list_1[:-2]
print ("Output of the list after right rotate by 2 : "+ str(list_1))
list_1 = list_1[1:] + list_1[:1]
print ("Output of the list after left rotate by 1 : " + str(list_1))