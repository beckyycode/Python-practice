"""
Collection of genetics tools built with Ryan
"""
# ________________________________ CODON GENERATOR _______________________________________________

def codon_generator (x):
    """
    Docstring for codon_generator
    
    :param x: RNA sequence
    """
    reading_frame = 3
    for base in range(0, len(x)):
        codon = x[base : base + reading_frame]

        print (codon)



# _________________________________ SEQUENCE SCANNER ___________________________________________________

def sequence_scanner (input_sequence,target_seq):
    """
    Docstring for sequence_scanner
    
    :param input_sequence: input a sequence of DNA or RNA, (or whatever) that you want to scan
    :param target_seq: input a particular small target sequence you are looking for in the larger input sequence

    """
    reading_frame = len(target_seq)
    for baseindex in range(0, len(input_sequence)):
        current_frame = input_sequence[baseindex : baseindex + reading_frame]
        if current_frame.upper() == target_seq.upper():
            print(current_frame.upper(), baseindex)


# ____________________________SEQUENCE COMPARISON____________________________________________________

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


# _________________________________________ mRNA TRANSCRIPTION _____________________________________________

def mRNAtranscription (DNAinput):
    """
    Docstring for mRNAtranscription
    
    :param DNAinput: Input a string of DNA and it will be transcribed into complimentary RNA
    """
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

# __________________________________BASE PAIR COUNTER_______________________________________________________

def basepaircounter (inputdata):
    """
    Docstring for basepaircounter
    
    :param inputdata: Input a DNA/RNA sequence to find it's length
    """

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

# __________________________________ CLEAN DATA _____________________________________________________________

def clean_data(data):
    """
    Docstring for clean_data, puts all sequences in uppercase, removes numbers and spaces
    
    :param data: Input nucleotide sequence that contains things like spaces and numbers that need to be removed
    """
    base_pairs = ["a", "t", "g", "c", "u"]
    newdata = ""
    for character in data:
        if character.upper() == "A" or character.upper() == "T" or character.upper() == "G" or character.upper() == "C" or character.upper() == "U":
            newdata = newdata + character.upper()
    return newdata
# __________________________________________________________________________________________________________________
# __________________________________________________________________________________________________________________
# __________________________________________________________________________________________________________________
# __________________________________________________________________________________________________________________
# __________________________________________________________________________________________________________________
# __________________________________________________________________________________________________________________
# __________________________________________________________________________________________________________________
