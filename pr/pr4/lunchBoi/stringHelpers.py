def heightHelper(string):
    h = string.count("\n") + 1
    if string[-2:] == "\n":
        h -= 1
    return h

def widthHelper(string, w=0):
    if not "\n" in string:
        if len(string) > w:
            return len(string)
        else:
            return w
    else:
        i = string.index("\n")
        if len(string[:i]) > w:
            w = len(string[:i])
        i += 1
        string = string[i:]
        return widthHelper(string, w)
