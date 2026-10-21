#!/bin/bash
# This script will give you the reverse, the compliment, and the reverse compliment of a DNA sequence.

while true
do
    read -p "Enter your DNA sequence: " seqq
    
    if [[ "$seqq" == "" ]]; then break; fi

    echo "Your original sequence is $seqq "

    echo "Reverse of your sequence: $(echo "$seqq" | rev)"

    echo "Compliment of your sequence: $(echo "$seqq" | tr ACTG TGAC)"

    echo "Reverse compliment of your sequence: $(echo $seqq | rev | tr ACTG TGAC)"
    
done