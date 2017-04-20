def transpose(infile, outfile):
    with open(infile, "r") as infile, open(outfile, "w") as outfile:
        dict = {}
        header = infile.readline()
        header = header.split(" ")
        header.reverse()
        header[0] = str(int(header[0]))
        i = 1
        for line in infile:
            if line != header:
                line = line.split(" ")
                line[-1] = str(int(line[-1]))
                dict[i] = line
                i += 1
        width = i
        outHead = " ".join(header) + "\n"
        outfile.write(outHead)
        for i in range(len(dict[1])):
            line = []
            for j in range(1, width):
                line.append(dict[j][i])
            line = " ".join(line) + "\n"
            outfile.write(line)
