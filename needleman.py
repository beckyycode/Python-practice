# Needleman-Wunsch Global Sequence Alignment

MATCH = 1
MISMATCH = -1
GAP = -1


def needleman_wunsch(seq1, seq2):

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    score = [[0 for _ in range(cols)] for _ in range(rows)]
    traceback = [["" for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        score[i][0] = i * GAP
        traceback[i][0] = "up"

    for j in range(1, cols):
        score[0][j] = j * GAP
        traceback[0][j] = "left"

    for i in range(1, rows):
        for j in range(1, cols):

            if seq1[i - 1] == seq2[j - 1]:
                diagonal = score[i - 1][j - 1] + MATCH
            else:
                diagonal = score[i - 1][j - 1] + MISMATCH

            up = score[i - 1][j] + GAP
            left = score[i][j - 1] + GAP

            best_score = max(diagonal, up, left)
            score[i][j] = best_score

            if best_score == diagonal:
                traceback[i][j] = "diagonal"
            elif best_score == up:
                traceback[i][j] = "up"
            else:
                traceback[i][j] = "left"

    aligned_seq1 = ""
    aligned_seq2 = ""

    i = len(seq1)
    j = len(seq2)

    while i > 0 or j > 0:

        if i > 0 and j > 0 and traceback[i][j] == "diagonal":
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            i -= 1
            j -= 1

        elif i > 0 and traceback[i][j] == "up":
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1

        else:
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    final_score = score[len(seq1)][len(seq2)]

    return aligned_seq1, aligned_seq2, final_score


sequence1 = input("Enter the first DNA sequence: ").upper()
sequence2 = input("Enter the second DNA sequence: ").upper()

aligned1, aligned2, final_score = needleman_wunsch(sequence1, sequence2)


# Build the middle line
match_line = ""

for base1, base2 in zip(aligned1, aligned2):

    if base1 == "-" or base2 == "-":
        match_line += " "

    elif base1 == base2:
        match_line += "|"

    else:
        match_line += "."


print("\nAlignment:\n")

print("Seq 1:  " + aligned1)
print("        " + match_line)
print("Seq 2:  " + aligned2)

print("\nFinal alignment score:", final_score)