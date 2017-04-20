def eligible(infile, outfile):
    eligible = []
    with open(infile, "r") as infile, open(outfile, "w") as outfile:
        for line in infile:
            s = line.split(", ")
            if int(s[1]) >= 18:
                outfile.write(line)
