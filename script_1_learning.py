"""
 VARIABLE:  can associate a name with a specific piece of data 
  x = y
 can contain data types such as
 numbers, 123
 strings (text, must be in quotes)
 bullions (true or false, not in quotes)
 None (no value)
 Example x = 123   or   var = "abc"   or    cat = True   or    age = None 



 

 LIST: an ordered list of values.
 Ex:
 mygrades = ["A", "B", "A", "A-"]
 shopping_list = ["apples", "banana", "carrot", "orange"]
lists can contain muitples types, like numbers, strings, bullions ect.





 DICTIONARY (called objects in other languages)
 associating values with each other (can associate different value types)
 Ex:
 Sadie = {
   "name": "Sadie",
   "age": 10,
   "color": "cream",
   "cat": True,
}
 Sasha = {
   "name": "Sasha",
   "age": None,
   "color": "black",
   "cat": True,
}



 LIST OF DICTIONARYS
 Pets = [Sadie, Sasha]

 

 

 
 LOOP: going through the list
 ex:
 for Var(new variable, can be named anything) in list(existing list):
   command, like print or add properties from the dictionary (ex "Name": "Sadie")


 


IFSELSE: (else is not required)
ex:

 if blank:
   action
 else:
   other action


   


 
FUNCTIONS
 print is a function
 you can also DEFINE a function with def
 EX:

 def myfunction():
    print("hello")

OR

def mynewfunction():
    return 1 (or other numbers)
 

 a function can take arguments or parameters - like a mathematical function like f(x)

example:

def add(a, b):
    return a + b

 sum = add(1,1)

 



 

 

 



 CODE EXAMPLE: SHOPPING LIST




orange = {
    "cost": 1,
    "needed?": True,
}

deoderant = {
    "cost": 5,
    "needed?": True,
}

croissant = {
    "cost": 3,
    "needed?": False,
}

grocery_budget = 10

shopping_list = [orange, deoderant, croissant]

total = 0
for item in shopping_list:
    print (item["cost"])
    total = total + item["cost"]

print ( "Total equals", total)

if total > grocery_budget:
    print("Over Budget")
else:
    print("Cha ching baby")








    
CODE EXAMPLE NO 2 write a function to multiply two numbers




def multiplication(a,b):
    return a * b

answer = multiplication(6,7)

print (answer)


CODING EXAMPLE NO 3, bigger than 10 return true smaller than 10 return false



def bigboi(a):
    if a > 10:
        return "BIGBOIIIII!"
    else:
        return "micropenis"

Ryan = bigboi(19)

print (Ryan)

EX 4 add a list of numners

def sum(list):
    total = 0
    for number in list:
        print (number)
        total = total + number
    return total

numbers = [1, 2, 3, 4, 5]

answer = sum(numbers)

print (answer)


the variable in sum represents a list in this case (but could also stand in for a varable)
the number in list is each individual item in the list, in this case numbers
total is it's own variable, starting at zero, used to add the numbers in the list
to add the numbers in a particular list, type answer = sum(nameoflist)
then print answer
or you can simply print (sum(numbers))


    
EXAMPLE 5 does this list only have true values in it?

the return function will happen as soon as it encounters the set condition (like a flase value) and will end the loop. which is why we can say if "truth" = false return False
and then in the line right after this return true, since this will only happen if no False value is encountered in the list



Bullions = [True, False, False]

def alltrue (list):
    for truth in list:
        print (truth)
        if truth == False:
            return False
    # loop is over, we did not return so all values were true
    return True

if alltrue(Bullions) == True:
    print ("All True")
else:
    print ("Liar pants")



EXAMPLE NO 6 SHOPING LIST FUNCTION - is the list in budget?"""



orange = {
    "cost": 1,
    "needed?": True,
}

deoderant = {
    "cost": 5,
    "needed?": True,
}

croissant = {
    "cost": 3,
    "needed?": False,
}

grocery_budget = 10

shopping_list = [orange, deoderant, croissant]

total = 0
for item in shopping_list:
    print (item["cost"])
    total = total + item["cost"]

print ( "Total equals", total)

if total > grocery_budget:
    print("Over Budget")
else:
    print("Cha ching baby")
#^^^^^ this will print another cha ching baby

#make a funciton called in budget

def in_budget(budget,mylist):
    total = 0
    for item in mylist:
        total = total + item["cost"]
    if total > budget:
        return ("over budget")
    else:
        return ("chaching baby")
# not putting return in the function will cause it to return the value None, so make sure to return at the end of the function

Beccas_answer = in_budget(11,shopping_list)

Ryans_answer = in_budget(8,shopping_list)

print (Ryans_answer, Beccas_answer)