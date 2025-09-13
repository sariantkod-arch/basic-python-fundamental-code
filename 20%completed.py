#Chapter 1

# DATARULE

a = 1 # a is an integer
b = 5.22 # b is a floating point number
c = "Harry" # c is a string
d = False # d is a boolean variable
e = None # e is a none type variable

# VARIABLERULE

a = 23  # invalid  'a'
kodkumad = 435  # invalid kod kumad
harry45 = 34  # invalid 45harry
sameer_kumar = 45  # sameer-kumar   invalid or sameer$kumar
_45 = 34 #invalid  42 

# MATHEMATHICS OPERATOR

# 1)  ARITHMATIC OPERATOR
a = 2
b = 5

print(f"then, add {a+b}\nsubtract {a-b}\nmultiply {a*b}\ndivide {a/b}\ndivision (roundoff) { a//b}\nexponential {a**b}\nremainder {a%b}")

# ASSIGNNMENT OPERATOR

a = 4-2 # Assign 4-2 in 
print(a)
b = 6
# b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print(b) # OUTPUT (3)
print (a+b) #output (5)

# COMPARISION OPERATOR

a = 5 
b = 4
d = 5==5  # (==) for equal sign
# output always come in true or false as this is for comparision
print(d)  
print(5<=4) # bigger or equal to
print(5!=5)  # (!=) is not equal sign

# LOGICAL OPERATOR

#tell if value is true or not
e = True or False  # value of e is true in physics
print(e)

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and' 
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))  # vive output opposite to true value, in tbis case 'FALSE'

# QUESTION

# 1) write a programme "twinkle twinkle little star" peom.
# 2) write table of 5 using RHEL or other way.
# 3) install a external module and use it to perform an operation of your interest.
# 4) write a pythone programe to print the content of the directory.

# CHAPTER 2

# TYPE () FUNCTION AND TYPE CASTING
a = 2 
p = type(a) # class<int>
print(p)

# To change type 
a = "31.2"  # class <str>
b = float(a) # a but the type should be float
t = type(b) 
print(t)

# INPUT( ) FUCTION
a = int(input("Enter number 1:  "))
b = int(input("Enter number 2:  "))

print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)

# QUESTION

# 1)  write a programe to add two number
# 2) write a programe to find remainder when a number is divided by 2
# 3) check the type of variable assigned using input() variable
# 4) use comparision assignment to find whether 'a' is greater than 'b' or not.  take 'a = 34'  and 'b = 80'
# 5) write a programe to find an average of two number entered by user
# 6) write a programe to calculate square of a number entered by user

# CHAPTER 3

# STRING SLICING

#we count any word in python as " from starting point [0,infinity)"  if we count "from bacword;[-1,-infinity)"

name = 'harry' # from starting (0,1,2,3,4) from back (-1,-2,-3,-4,-5)

# for slicing word
print(name[1]) # output 'a'
#multiple word slicing between two point
print(name[0:4]) # start from index 0 all the way till 4 (Excluding 4): "output 'harr"

# If you see in any code in which word slicing written as
print(name[-3:-1])
# we first need to transform it like number that is counted from starting,  in this case total number of word 5 Now, [5 +(-3):5 +(-1)]
print(name[2:4])
print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])
print(name[1:5])

# for jump slicing
a = 'sariant kod'
print(a[0:12:2])  # last 2 is for jump
#output 'sratkd' as after each 2 jump (s - > r -> a -> t -> k -> d)

# STRING FUCTION

# ===============================================
# Python String Methods (Most used -> Least used)
# ===============================================

text = " sariant kod "
text2 = ' DOCA '
num_text = "12345"
mix_text = "harry12345"
title_text = "DIMENSION"
multi_line = "harry\nsariant\nkod"

# 🔹 MOST USED STRING METHODS
print("1. upper()       :", text.upper())        # Convert to UPPERCASE

print("2. lower()       :", text2.lower())        # Convert to lowercase

print("3. strip()       :", text.strip())        # Remove spaces from both ends

print("4. replace()     :", text.replace("sariant", "Python").replace( "kod","book"))  # Replace substring

print("5. split()       :", text.split())        # Split into list of words

print("6. join()        :", "-".join(["a","b","c"])) # Join list into string with separator

print("7. find()        :", text.find("world")) # Find index of substring (-1 if not found)
#for find multiple word at same time we can do seprately or use "for" and "in"
for word in ["world", "sariant kod"]:
    print(f"Find '{word}' :", text.find(word))
    
print("8. startswith()  :", text.startswith("  h"))  # Check if string starts with substring
print("9. endswith()    :", text.endswith("od  "))  # Check if string ends with substring
# startwith and end with give output in "true or false"

print("10. format()     :", "My name is {}".format("Alice"))  # Insert values into placeholders



# 🔹 FREQUENTLY USED CHECK METHODS
print("11. isdigit()    :", num_text.isdigit())   # True if all characters are digits

print("12. isalpha()    :", "hello".isalpha())    # True if all characters are alphabets

print("13. isalnum()    :", mix_text.isalnum())   # True if only letters and numbers

print("14. isspace()    :", "   ".isspace())      # True if only whitespace

print("15. islower()    :", text.islower())       # True if all lowercase
print("16. isupper()    :", text2.isupper())    # True if all uppercase

print("17. istitle()    :", "Hello World".istitle()) # True if title case




# 🔹 MODERATELY USED FORMATTING + SEARCH
print("18. title()      :", title_text.title())   # Convert to Title Case

print("19. capitalize() :", text.capitalize())    # First character uppercase, rest lowercase

print("20. swapcase()   :", "Hello".swapcase())   # Swap upper <-> lower

print("21. count()      :", text.count("s"))      # Count occurrences of substring

print("22. index()      :", text.index("kod"))  # Like find(), but raises error if not found

print("23. rfind()      :", text.rfind("a"))      # Find last occurrence

print("24. rindex()     :", text.rindex("s"))     # Like rfind(), but error if not found

print("25. rsplit()     :", text.rsplit())        # Split from the right

print("26. partition()  :", text.partition("world")) # Split into (before, match, after)

print("27. rpartition() :", text.rpartition("hello")) # Partition from the right




# 🔹 ALIGNMENT / PADDING METHODS
print("28. center()     :", "hi".center(10, "-"))  # Center text with padding

print("29. ljust()      :", "hi".ljust(10, "-"))   # Left align with padding

print("30. rjust()      :", "hi".rjust(10, "-"))   # Right align with padding

print("31. zfill()      :", "42".zfill(5))         # Pad with zeros on the left



# 🔹 STRING CLEANUP
print("32. lstrip()     :", text.lstrip())         # Remove spaces on the LEFT

print("33. rstrip()     :", text.rstrip())         # Remove spaces on the RIGHT




# 🔹 MULTI-LINE STRING METHODS
print("34. splitlines() :", multi_line.splitlines()) # Split into lines




# 🔹 ADVANCED / RARELY USED
print("35. casefold()   :", "HELLO".casefold())    # Aggressive lowercase (for comparisons)
print("36. encode()     :", text.encode())         # Encode string to bytes
print("37. expandtabs() :", "a\tb".expandtabs(4))  # Replace tabs with spaces
print("38. isascii()    :", "hello".isascii())     # True if all characters are ASCII
print("39. isdecimal()  :", "123".isdecimal())     # True if decimal characters
print("40. isnumeric()  :", "Ⅳ".isnumeric())       # True if numeric (includes Unicode)
print("41. isidentifier():", "variable1".isidentifier()) # True if valid Python variable name
print("42. isprintable():", "hello".isprintable()) # True if printable characters
print("43. maketrans() & translate():",
      "hello".translate(str.maketrans({"h":"H","e":"E"}))) # Map characters to new ones

# 🔹 NEW IN PYTHON 3.9+
print("44. removeprefix():", "unhappy".removeprefix("un")) # Remove prefix if present
print("45. removesuffix():", "running".removesuffix("ing")) # Remove suffix if present

# 🔹 RARELY USED BUT EXISTS
print("46. format_map() :", "{x} + {y}".format_map({"x":1,"y":2})) # Similar to format()


# ESCAPE SEQUENCE CHARACTER

# Newline -> moves text to the next line
print("Hello\nWorld")  
# Output:
# Hello
# World


# Tab -> adds a horizontal tab space
print("Hello\tWorld")  
# Output: Hello    World


# Double quote inside double quotes -> allows " inside "
print("He said \"Python is fun\"")  
# Output: He said "Python is fun"


# Single quote inside single quotes -> allows ' inside '
print('It\'s a good day')  
# Output: It's a good day


# Backslash itself -> print \
print("This is a backslash: \\")  
# Output: This is a backslash: \


# Unicode -> print special characters (emoji, symbols)
print("Heart: \u2764  Smile: \U0001F600")  
# Output: Heart: ❤ (16bit)  Smile: 😀 (32bit)


# QUESTION



#CHAPTER4

#LIST

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])  #output "grapes"
print(friends[1:4])  #output "orange,5,335.06"

#LISTMETHOD

L1 = [1,2,8,5,56,33]
value = L1.pop(3)  # remove 5 from list
print(value)
print(L1)

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

# --- Most Used List Methods ---

print(friends.append('Banana'))
print(f" :Adds 'Banana' at the end of the list:    {friends}")

friends.insert(2, "Mango")
print(f"Inserts 'Mango' at index 2:     {friends}")

friends.extend(["Cherry", 99])
print(f" Adds multiple elements at the end :         {friends}")

friends.remove("Orange")
print(f" Removes first occurrence of 'Orange':        {friends}")

friends.pop()
print(f"Removes and returns last element (here: 99:     {friends}")

friends.count("Aakash")
print(f"Counts how many times 'Aakash' appears:    {friends}")

friends.index("Rohan")
print(f"Finds index of first occurrence of 'Rohan':    {friends}")

friends.reverse()
print(f" Reverses the list in place :        {friends}")

friends.sort(key=str)
print(f"Sorts the list (here we convert all to str to avoid error with mixed types):    {friends}")

friends.copy()
print(f" Creates a shallow copy of the list:        {friends}")

friends.clear()
print(f"Removes all elements from the list:    {friends}")

#TUPLET

a = (1,45,342,3424,False, "Rohan", "Shivam")
print(a)
print(type(a))

#TUPLETMETHOD

a = (1,45,342,3424,False, 45, "Rohan", "Shivam")
print(a) 

no = a.count(45)
print(no)    # 2

i = a.index(3424)
print(i)  # 3

print(len(a)) #  8 len

#DICTIONARY

d = {} # Empty dictionary
marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}


print(marks, type(marks)) # class<dic>
print(marks["Harry"])  # 100

#DICTO  METHOD

marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23,
    0: "Harry"
}

# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry": 99, "Renuka": 100})
# print(marks)

print(marks.get("Harry2")) # Prints None
#print(marks["Harry2"]) Returns an error


#SET

e = set() # Dont use s = {} as it will create an empty dictionary
s = {1, 5, 32, 54,5, 5, 5} 


print(s)

#SETMETHOD

s = {1, 5, 32, 54,5, 5, 5, "Harry"}

print(s, type(s))

s.add(566)
print(s, type(s))
s.remove(1)
print(s, type(s))

s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2))
print(s1.intersection(s2))

#CONDITION

a = int(input("Enter your age: "))

# If_else_CONDITION
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

else:
    print("You are below the age of consent")


print("End of Program")

#if_else_elif CONDITION

a = int(input("Enter your age: "))

# If elif else ladder
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")

elif(a==0):
    print("You are entering 0 which is not a valid age")    

else:
    print("You are below the age of consent")


print("End of Program")

#MULTIPLE_if_STATMENT

a = int(input("Enter your age: "))

# If statement no: 1
if(a%2 == 0):
    print("a is even")
# End of If statement no: 1

# If statement no: 2
if(a>=18):
    print("You are above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are entering an invalid negative age")  

else:
    print("You are below the age of consent")
# End of If statement no: 2

print("End of Program")



#LOOP

print(1)
print(2)
print(3)
print(4)
print(5)

# The same task can be done like this:
for i in range(1, 6):
    print(i)
    
    #WHILE LO0P
    
i = 1

while(i<51):
    print(i)
    i +=1 # or i = i + 1
'''
Output:
1
2
3
4
5
'''
#LISTUSINGEWHILELOOP

l = [1, "Harry", False, "This", "Rohan", "Shubham", "Shubhi"]

i = 0

while(i<len(l)):
    print(l[i])
    i +=1

#FORLOOP

for i in range(4):
    print(i)

#FORLOOPILETRATE

## For Loop with Lists
l = [1, 4, 6, 234, 6, 764]
for i in l:
    print(i)

## For Loop with Tuples
t = (6, 231, 75, 122)
for i in t:
    print(i)

## For Loop with Strings
s = "Harry"
for i in s:
    print(i)
    
#LISTUSINGFOR

l= [1,7,8] 

for item in l:
    print(item)

else:
    print("done") # this is printed when the loop exhausts!
    
#BREAK AND CONTINUE

for i in range(100):
    if(i == 34):
        break # Exit the loop right now
    print(i)

for i in range(100):
    if(i == 34):
        continue # Skip this iteration
    print(i)    

#PASS

for i in range(645):
    pass



i = 0
while(i<45):
    print(i)
    i += 1



