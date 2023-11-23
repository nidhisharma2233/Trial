#1. Check if a given string is a palindrome or not.
string1=input("enter string")
string2=string1[::-1]
if string1==string2:
    print("string is palindrome")
else:
    print("string is not palindrome")

