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






BUILD A CHARACTER COUNTER:

my_string = "Hello"

def charactercounter (string):
    total = 0
    for character in string:
        total += 1
    return total

character_count = charactercounter (my_string)
print (character_count)






LEN:


my_string = "Hello"
length_of_my_string = len(my_string)
print (length_of_my_string)

output:
5







INDEX INTO A STRING

my_string = "Hello"

print (my_string[0])

output: H






# zip       -> zippers two lists together
# print     -> prints text or whatever
# len       -> returns the length of a string or list
# enumerate -> zippers a list with its indexes(the position in the list, like zero, or 7, ect.)













EXAMPLES



list_1 = ["hello", "word", "three"]
list_2 = [4, 5, 6]

yippy = len(list_1)
yo = range(0, yippy)
yehaw = list(yo)

# print(yehaw)


my_string = "Hello"

print("FIRST")
# THIS HERE:
for index in range(0, len(my_string)):
    my_letter = my_string[index]
    print("index  =", index)
    print("letter =", my_letter)


print("SECOND")
# IS JUST DOING THE SAME AS THIS:
print(my_string[0])
print(my_string[1])
print(my_string[2])
print(my_string[3])
print(my_string[4])










Using an index to scan codons:



dna = "ttaattggcccttaattctatcatttaattggcccttaattctatcatttaattggcccttaattctatcatttaattggcccttaattctatcatttaattggcccttaattctatcat"

reading_frame = 3


for index in range(0, len(dna)):
    codon = dna[index : index + reading_frame]
    print(codon)



    




    




# BUILT IN PYTHON FUNCTIONS:
# zip             -> zippers to lists together
# print           -> prints text or whatever
# len             -> returns the length of a string or list
# enumerate       -> zippers a list with its indexes
# list            -> will try to turn what you give it into a list
# range(n, m)     -> makes a list from n to m




"""

