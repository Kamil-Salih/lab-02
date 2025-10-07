#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 05/10/2025

line_number=1
with open('sample.txt', 'r') as f:
    for line in f:
        print(f"{line_number}: {line.strip()}")
        line_number=line_number+1
        