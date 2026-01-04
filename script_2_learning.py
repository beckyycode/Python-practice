"""
NOTES

one equal sign = is an assignment as in "this is that"
two equal signs == are a comparison as in "is this, that?"

cat = "sadie"

if cat == "sadie":
    print("I'm baby")
elif cat == "sasha":
    print ("I'm scabby")
elif cat == "Marcy"
    print ("LET ME OUTSIDE")
else:
    print ("meow meow meow meow")


elif (else if) as in, it is another "if" in the case that it is not the first "if" and it goes in order, so only one will occur (the most high up one in the list)

"""




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


#make a funciton called in budget

def in_budget(budget,mylist):
    total = 0
    for item in mylist:
        if item["needed?"] == True:
            total = total + item["cost"]
    if total > budget:
        return "You broke son, get money, it's not hard. I'm tired of this broke mentality, get better mentality, it's not hard."
    else:
        for item in mylist:
            if item["needed?"] == False:
                total = total + item["cost"]
    if total > budget:
        return "No treats this time"
    else:
        return "yee boiiiii!"
        
# not putting return in the function will cause it to return the value None, so make sure to return at the end of the function

Sadies_answer = in_budget(0,shopping_list)

Beccas_answer = in_budget(grocery_budget,shopping_list)

Ryans_answer = in_budget(8,shopping_list)

print ("Sadie:", Sadies_answer, "\nRyan:", Ryans_answer, "\nBecca:", Beccas_answer)



"""alternative answer to the problem above, say if you are in budget for needed and non needed items



def in_budget(budget, list):
    required_total = 0
    nice_to_have_total = 0

    for item in list:
        if item["needed"]:
            required_total = required_total + item["cost"]

#^^^(this line has the condition that the item has to be "needed" so it only adds items that meet this condition)

        nice_to_have_total = nice_to_have_total + item["cost"]

#^^(this line adds all items regardless of if they are needed or not)

    if nice_to_have_total < budget:
        return "we rich bitch"
    elif required_total < budget:
        return "aight we ok"
    else:
        return "damn im broke son"


sadie_answer = in_budget(0, shopping_list)
ryan_answer = in_budget(8, shopping_list)
becca_answer = in_budget(22, shopping_list)

print("Sadie", sadie_answer)
print("Ryan", ryan_answer)
print("Becca", becca_answer)


"""






