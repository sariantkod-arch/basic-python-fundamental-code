#what is code
#It is just a language like english ,that is written by people in order to take with computer

#syntax js just like word
#in different programming language syntax can be varies but concept remain tbe same

#python can be  used every where
#SQL is querying language
#JavaScript, HTML , CSS arre language of web ,learn to create website from scratch

# in this programe ,we are gonna learn PYTHON 


# Remember about syntax and every small detail during writing code as even smallest mistake can be fatal.

#<<<<<<<<<<<LET START>>>>>>>>>>>




# most common 
print("hello,world!")   # double quote remember

#for multiple line python use three double quote
print("""hi,everyone i am begginer in coding
and i am very enthusiasm to write my own code from starting ,and contnue
to write as i learn""")

#this is (#) sign for comment we write comment for telling other what that code used for and comment does not abow in output

# for multiple line comment similar to print use('  '   '  )  triple single quote 
'''doctor
                    djdn
                                        djdidj
                                        
                                        dj '''


# why we need multiple line triple quote because when we cut halfway through a line and continue to write python  take it as something new unlike single double quote wher you continue to write without breaking line. so, when you take multiple line python with take it in same code.(for example this comment)



# DATA_RULE 
#[data type is for DIFFERENTIATING between number,text,etc]

# Everything in python has DATATYPE and  CLASS

# FUNDAMENTAL_ DATA_ TYPE
a = 1 # a is an integer
b = 5.22 # b is a floating point number(decimal)

c = "sariantkod" # c is a string ( you can also use single quote instead of  double no problem)

d = False # d is a boolean variable(give output in True{capital T} or False)
e = None # e is a None{capital N} type variable

# some COMPLEX _CLASS
s = set()  #set
c = ()            #dictionary
li = [2,"handsome",7.0,True]     #list
te = (2,9,8.0,"sariant")    #tuple



# VARIABLE_RULE
# variable store data in memoey, think it as container that hold data which can changed later in peograme.'

a = 23  # invalid  'a'(NO use of Double quotes and Single quote)

kodkumar = 435  # invalid kod kumar (no gap between character)

harry45 = 34  # invalid 45harry (no number at starting)

sameer_kumar = 45  # sameer-kumar   invalid or sameer$kumar  (don't use dash;or special character')

_45 = 34 #invalid  42 
# you can use underscore instead of hyphen


# MATHEMATHICS_OPERATOR

# 1)  ARITHMATIC OPERATOR

# output of two integer is intergers                               # if one;integer and other floating then output floting
#division(/) output always floting but it's not true for roundoff division(//).

a = 2
b = 5

print(a + b)       # addition
print (a - b)          #subtraction
print(a * b)        #multiplication
print(a / b)            #division 
print(a // b)        #floor division (change                            dicimal division into                        integer by taking taking  most                significant interger  example :->                                    "2.99" it will give "2" answer)
print(a ** b)            #exponential
print(a % b)           #remainder(modulus)
print(round(a/b))   # for roundoff division


# it is important to know order of execution of python operator (highest to lowest ) just like in math

#  first () this is parenthesis

# then **

#  after   *  ,  /    ,    //    ,    %   (from left to right it depend on you how you write equatiion in python)

#and last       +   ,    -   



# ASSIGNNMENT_OPERATOR(=      or     +=     or      -+     or     ==)

a = 4-2 # Assign 4-2 in 
print(a)
b = 9
# b += 3 # Increment the value of b by 3 and then assign it to b
b -= 3 # Decrement the value of b by 3 and then assign it to b
print(b) # OUTPUT (6)
print (a+b) #output (8)


# before we go futher some basic note,        when we use two same variable ,python take new variable and terminate previous.

a = 3 
a = 10  # python take value of a always 10 and never 3 
b = 4
print(a+b) #(output will be 14 instead of 7)


#  SHORTHAND FOR ARITHMATICS

a = 5
b = 6

a += b        # a = a+b(11)

a += b        # a = a+b(17)

a += 20  # a = a + 20  (25)


# COMPARISION _OPERATOR

a = 5 
b = 4
d = 5==5  # (==) for equal sign
# output always come in true or false as this is for comparision
print(d)  
print(5<=4) # bigger or equal to
print(5!=5)  # (!=) is not equal sign


# LOGICAL_ OPERATOR

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




#some basic knowledge
# MODULE :>- A module in Python is just a file that contains Python code (functions, variables, or classes created by other)

#Think of it like a toolbox 📦. Instead of writing everything yourself, you can use tools already inside that box.

# you can create module but we take other people built code to make our work easier and faster


#PIP:>- Imagine you need a tool (module) that is not already in Python.
#With pip, you can download and install extra toolboxes
# you can't create pip(if you want you need very advanced knowledge)

''' NOTE :--  
A good coder not only know how to solve PROBLEM but also how to follow INSTRUCTION.
             BELOW there is quostion try to solve by your own and if you get any problem USE CAN USE CHATGPT OR ANY AI only for LEARNING PURPOSE.
             
# QUESTION

# 1) write table of 5 using RHEL or other way.

# HOW TO SOLVE FOLLOW INSTRUCTION

Open Python in RHEL
Start your terminal in RHEL (Red Hat Enterprise Linux).
                Type python3 (or python) to open the Python interpreter.
                In Python, * means multiplication
Try printing 5 * 3 to see how it works.
    now ,comple table 5
    

# 2) install a external module  "pyjokes" and use it to perform an operation of your interest.

#HOW TO SOLVE FOLLOW INSTRUCTION

#Install an external module and use it
Open your terminal in RHEL.                                           
Use pip (Python package manager) to install the module.

Example: pip install <module_name>.
Once installed, open Python and import that module using import. 

    Explore the module’s functions (you can use help(module_name)).                       
    Call a function from the module to perform some operation.
   
Example: In pyjokes, there is a function that gives you a joke.


# 3) write a pythone programe to print the content of the directory.

#HOW TO SOLVE FOLLOW INSTRUCTION

Think about what a directory means (a folder that contains files).                                                                Python has a built-in module to interact with the operating system'''



'''
#NOTE

# Before moving further lets look at common defination (most people make mistake in) difference between MODULE , FUNCTION()  ,  ALGORITHM

1)  MODULE :-->  File or COLLECTION of File that contain function() , class ,and variable
example:
    
 import math   #math is module
             print(math.sqrt(16))  # using                                   function inside math module
             
2) FUNCTION() :-->  Fuction allows us to BREAK up our program into MINI PROGRAM ,each with specific task that we need.
suppose we need to make spaggeti ,

step to follow:
 a) take a skillet
 b) take one  up water and boil it
 c) take raw spaggeti and cook it in water
 d) use some salt and pepper
 e) serve the food and then eat.
 
so, much work  ,Sppose we have a function called spaggeti_cook witth all instrution written in it .then,instead of writing long instrution we just write function(spaggeti_cook) and it work done.

A function is like Machine thht perform specific task. you can give INPUT(ARGUMENT) ,if its work then it will give you back OUTPUT(RETURN VALUE)

example: 
    def add (a,b):   # function defination
            return a + b
 
 print(add(3,5))   # function call
 
 
3) ALGORITHM :--> an algorithm is                         STEP-BY-STEP PROCESS or RECIPE for SOLVING PROBLEM.
it is NOT CODE Itself ,but rather the logic or method that you can later write as code
'''



# TYPE () FUNCTION_AND_TYPECASTING

# This tell what type of data that your variable contain

a = 2 
p = type(a) # class<int>
print(p)

# To change type of type inside variable
a = "31.2"  # class <str>
b = float(a) # a but the type should be float
t = type(b) 
print(t)


# INPUT( ) FUCTION

# you can tell user what he want to fill in some bracket
a = int(input("Enter number 1:  "))
b = int(input("Enter number 2:  "))

print("Number a is: ", a)
print("Number b is: ", b) 
print("Sum is ", a + b)

#always remember smallest sign you see




# QUESTION

'''
# 1)  write a programe to add two number

#HOW TO SOLVE FOLLOW INSTRUCTIO

Ask the user to enter two numbers.

Store them in variables.

Add them using the + operator.

Print the result



# 2) write a programe to find remainder when a number is divided by 2

#HOW TO SOLVE FOLLOW INSTRUCTIO

Take a number from the user.

Use the modulus operator % to find the remainder.

Print the remainder.



# 3) check the type of variable assigned using input() variable

#HOW TO SOLVE FOLLOW INSTRUCTION

Use input() to take a value from the user.
Assign it to a variable.

Use the type() function to check what kind of variable it is.

Print the type.



# 4) use comparision assignment to find whether 'a' is greater than 'b' or not.  take 'a = 34'  and 'b = 80'

#HOW TO SOLVE FOLLOW INSTRUCTION

Assign a = 34 and b = 80.

Use a comparison operator (>).

Print the result (True/False).



# 5) write a programe to find an average of two number entered by user

#HOW TO SOLVE FOLLOW INSTRUCTION

Ask the user for two numbers.

Add them together.

Divide the result by 2.

Print the average.



# 6) write a programe to calculate square of a number entered by user

#HOW TO SOLVE FOLLOW INSTRUCTION

Take a number as input from the user.

Multiply the number by itself.

Print the result as the square.
'''




# STRING _SLICING


#we count any word in python as " from starting point [0,infinity)"  if we count "from bacword;(-infinty,-1] 
# Always remember write from small number to biggest

name = 'Trump' #counting letter or number  from starting (0,1,2,3,4) from backward (-1,-2,-3,-4,-5)

# for slicing word
print(name[1]) # output 'T' ( count T -> 0 (first number) ,R -> 1   (second number)     we need to exclude 1 according to rule)

#word slicing between two point
print(name[0:4]) # start from index 0 all the way till 4 (Excluding 4): "output 'harr"

# If you see in any code in which word slicing written as
print(name[-3:-1])
# we first need to transform it like number that is counted from starting,  in this case total number of word 5 Now, [5 +(-3):5 +(-1)] that is [2:4]
print(name[2:4])

print(name[:4]) # is same as print(name[0:4])
print(name[1:]) # is same as print(name[1:5])


# for jump slicing
a = 'sariant kod'
print(a[0:12:2])  # last 2 is for jump
#output 'sratkd' as after each 2 jump (s - > r -> a -> t -> k -> d), (even we count gap)


# STRING_ FUCTION

#string are unmutable that means we can only make new string but could never able to change existing one

#for editing existing string we use some built in python string function


# ===============================================
# Python String Methods (Most used -> Least used)
# ===============================================


text = " sariant kod "
text2 = ' DOCA '
num_text = "12345"
mix_text = "Trump12345"
title_text = "DIMENSION"
multi_line = "harry\nsariant\nkod"

# 🔹 MOST USED STRING METHODS
print("1. upper()       :", text.upper())        # Convert to UPPERCASE

print("2. lower()       :", text2.lower())        # Convert to lowercase

print("3. len()           :", len(text))        # for finding length of word ; remember len is not string fuction but global function that use everywher in code this is why it is written len(text)  instead of text,l.len()

print("3. strip()       :", text.strip())        # Remove spaces from both ends

print("4. replace()     :", text.replace("sariant", "Python").replace( "kod","book"))  # Replace substring

print("5. split()       :", text.split())        #       Split into list of words

print("6. join()        :", "-".join(["a","b","c"])) # Join list into string with separator

print("7. find()        :", text.find("world")) # Find index of substring (-1 if not found)

#for find multiple word at same time we9 can do seprately or use "for" and "in"
for word in ["world", "sariant kod"]:
    print(f"Find '{word}' :", text.find(word))
    
print("8. startswith()  :", text.startswith("  h"))  # Check if string starts with substring

print("9. endswith()    :", text.endswith("od  "))  # Check if string ends with substring
# startwith and end with give output in "true or false"

print("10. format()     :", "My name is {}".format("Alice"))  # Insert values into placeholders

#NOTE--:
#just remember most used string function and doesn't need to remember everything.


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



# ESCAPE _SEQUENCE_ CHARACTER


# inside string these sequenc character give you additional help and many time make your work more easier 

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




#LIST


# to create a list of something and  list can contain all kind of data type

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])  #output "grapes"
print(friends[1:4])  #output "orange,5,335.06"

#LIST_METHOD

#for making change in list 

L1 = [1,2,8,5,56,33]
value = L1.pop(3)  # remove 5 from list
print(value)
print(L1)

friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]


# --- Most_Used_ List_ Methods ---


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

""" same as list but tuplet are unmutable unlike list"""

a = (1,45,342,3424,False, "Rohan",
 "Shivam")
print(a)
print(type(a))

#TUPLET_METHOD


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
#to make yes or no decision 

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



