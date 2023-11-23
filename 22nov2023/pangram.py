#12. Check if a string is a pangram (contains all letters of the alphabet)

def ispangram(str2):
   alphabet = "abcdefghijklmnopqrstuvwxyz"
   for char in alphabet:
      if char not in str2.lower():
         return False
   return True

string1 = 'The five boxing wizards jump quickly.'
if(ispangram(string1) == True):
   print("Yes")
else:
   print("No")