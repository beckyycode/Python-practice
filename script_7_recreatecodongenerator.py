from script_5_basepaircomparison_practice_lacZ import lacopcombined
# print (lacopcombined)

"""

def codon_generator (x):
    reading_frame = 3
    for base in range(0, len(x)):
        codon = x[base : base + reading_frame]

        print (codon)


codon_generator(lacopcombined)

"""

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

sequence_scanner(lacopcombined,"GAA")











