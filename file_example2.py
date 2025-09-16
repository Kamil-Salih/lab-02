line_number=0
with open('sample.txt', 'r') as f:
    for line in f:
        line_number=line_number+1
        print(line_number,": ",line.strip())