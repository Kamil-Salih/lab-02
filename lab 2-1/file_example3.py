#Name: Kamil Salih
#Student number: C00307549
#Group: CW_KCCYB_B
#Date: 05/10/2025

#with open('output.txt', 'w') as f:
#    f.write("This is a new file.\n")
#    f.write("It has two lines.\n")


#with open('sample.txt', 'r') as f1:
#    with open('copy.txt', 'w') as f2:
#        f2.write(f1.read())


with open('sample.txt', 'r') as f1:
    with open('copy.txt', 'w') as f2:
        for line in f1:
            f2.write(line)
