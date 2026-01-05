"""we imported the function clean_data from our perious script 3
we then made a new file for the lac z gene data from genbank, and named that lac_z_gene_data
we then called the function clean_data using this lac z file as the input, and printed the result to check it was working.
use the words 
from __(file)___ import ____(function, variable, ect.)______

"""



from script_3_leaning_analyzelacz import clean_data
from lacOP_gene_data import lacOPgene

data = clean_data(lacOPgene)
print(data)



def basepaircounter (inputdata):

    total_a = 0
    total_t = 0
    total_g = 0
    total_c = 0
    #^^^^ this has to come before the for loop or they will keep getting reset at zero every time it loops

    for character in inputdata:

        if character == "a":
            total_a = total_a + 1
        elif character == "t":
            total_t = total_t + 1
        elif character == "g":
            total_g = total_g + 1
        elif character == "c":
            total_c = total_c + 1
        #^^^ this must be indented to be IN the for loop, if it isn't indented it will come "after" the for loop

    return "A:", total_a, "T:", total_t, "C:", total_c, "G:", total_g
    

#THIS IS WRONG  >>>>>  print ("A:", total_a, "T:", total_t, "C:", total_c, "G:", total_g)
# these variables only exist in the function, but can't be called outside of it (scoped to the function)^^^
answer = basepaircounter (data)
print (answer)
#^^ this is like saying y=f(x), print y

def mRNAtranscription (DNAinput):
    RNAoutput = ""
    for character in DNAinput:
        if character == "a" or character == "A":
            RNAoutput += "U"
        elif character == "t" or character == "T":
            RNAoutput += "A"
        elif character == "g" or character == "G":
            RNAoutput += "C"
        elif character == "c" or character == "C":
            RNAoutput += "G"
    return RNAoutput

RNAdata = mRNAtranscription(lacOPgene)
print ("mRNA transcript:", RNAdata)


#a = ""
#a = a + "test"
#
#a += "test"
#
#^^^^^^ this is a cleaner way to write a = a + "test"