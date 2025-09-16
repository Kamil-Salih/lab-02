with open('output.txt', 'w') as f:
    f.write("This is a new file.\n")
    f.write("It has two lines.\n")
    with open('sample.txt', 'r') as f2:
        content = f2.read()
        f.write(content)

