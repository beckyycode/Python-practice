"""
NOTES

zip function: takes two lists and joins them together one by one determined by their order in the sequence.


listA = [1, 2, 3]

listB = [4, 5, 6]

zipped = zip (listA, listB)

print (list(zipped))

"""



from lacOP_gene_data import lacOPgene, lacOP_FASTA
# print (lacOPgene, lacOP_FASTA)

from script_3_leaning_analyzelacz import clean_data

data = clean_data(lacOPgene)
FASTAdata = clean_data(lacOP_FASTA)
# print("SequenceA", data, "SequenceB", FASTAdata) 




def sequence_comparison (seqa, seqb):
    """
    Docstring for sequence_comparison
    
    :param seqa: Input any DNA/RNA sequence
    :param seqb: This sequence will be compared to seqa
    """
  
    zipped_seq = zip (seqa, seqb)
    # print (list(zipped_seq))
    combined_sequence = ""
    for charactera, characterb in zipped_seq:
    # charactera is the first vlaue in the set, and characterb is the second value in the set    

        if charactera.upper() == characterb.upper():
            combined_sequence += characterb
        else:
            combined_sequence += "X"
    return combined_sequence

lacopcombined = sequence_comparison (data, FASTAdata)
# print (lacopcombined)



#character a and character b separate the zipped values per set, so you have two per set, and then character a is the first and character b is the second
