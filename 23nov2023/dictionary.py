#Dictionaries
dict1 = {
  "subject": "math",
  "class": "12th",
  "year": 2020
}
#Print the "subject" value of the dictionary
print(dict1,"   ","subject value=",dict1['subject'])


#Duplicate values will overwrite existing values:
dict2 = {
  "subject": "math",
  "class": "12th",
  "year": 2020,
  "year": 2021
}
print("duplicate value=",dict2)
print("len func=",len(dict2))

#list data type
dict3 = {
  "subject": "math",
  "class": "12th",
  "year": 2020,
  "color":['red','blue','green']
}
print(dict3)


#Using the dict() method to make a dictionary
dictm = dict(name = "John", age = 36, country = "Norway")
print("dict method=",dictm)

#Get a list of the keys:
k = dict3.keys()
print("key value=",k)

#get a value of the keys
v= dict3.values()
print("value =",v)

#change the element
dict3["year"]=2022
print("after change=",dict3)


#update method
dict3.update({"year": 2023})
print('update method=',dict3)

#remove
dict3.pop("year")
print('after pop=',dict3)
dict2.popitem()
print(dict2)



#nested dictionary
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)