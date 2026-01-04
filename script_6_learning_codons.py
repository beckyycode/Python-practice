"""
NOTES

numbers are zero indexed in computer science (starts at zero not 1)
so position 4 will be the 5th number in the list.

an example involving a string:

my_string = "Hello"
print (my_string[1])

output: e

number out of range (ex: 99) will cause an error message




SLICE:

Ex

my_string = "Hello"
print (my_string[1:3])

output: ell


ENUMERATE:

my_string = "Hello"

for num in enumerate(my_string):
    print(num)

    
output ex:

0, H
1, e
2, l
3, l
4, o


for num, letter in enumerate(my_string):
    print (num)
    print (letter)

Output:
0
H
1
e
2
l
3
l
4
o





LEN:


my_string = "Hello"
length_of_my_string = len(my_string)
print (length_of_my_string)

output:
5
"""

my_string = "Hello"

def charactercounter (string):
    total = 0
    for character in string:
        total += 1
    return total

character_count = charactercounter (my_string)
print (character_count)

