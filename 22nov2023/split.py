
#13. Split a string into words and count the frequency of each word.
string2="hello i am nidhi and i am ready "
list2=string2.split()
print(list2)
dict1=dict()
for word in list2:
    if word in dict1:
        dict1[word]+=1
    else:
        dict1[word]=1
print(dict1)
