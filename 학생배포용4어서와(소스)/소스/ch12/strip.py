infile = open("proverbs.txt", "r")
for line  in infile:
    line = line.rstrip()
    print(line);
infile.close() 
