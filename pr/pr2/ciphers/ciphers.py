alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
import random
from math import log
random.seed()

#############################################################
# The following code doesn't need to be edited. It allows
# you to read a text file and store it in a single string,
# and also to write a single string to a text file. This is
# not an ideal way to work with files, but it will suffice
# for this assignment.
#############################################################

def file_to_string(filename):
    with open(filename, "r") as f:
        x = f.read()
    return x

def string_to_file(filename, s):
    with open(filename, "w") as f:
        f.write(s)



#############################################################
# A working Caesar cipher
#############################################################

def simplify_string(s): # can we do this more like a comprehension?
    output = ""
    for char in s:
        upper = char.upper()
        if upper in alpha:
            output += upper
    return output

def num_to_let(x):
    return alpha[x]

def let_to_num(a):
    return alpha.index(a.upper())

def shift_char(char, shift):
    char_index = let_to_num(char)
    shift_index = let_to_num(shift)
    out_index = char_index + shift_index
    if out_index >= 26:
        out_index = out_index - 26
    return alpha[out_index]

def caesar_enc(plain, key):
    cipher = ""
    for char in plain:
        cipher += shift_char(char, key)
    return cipher

def caesar_dec(cipher, key):
    if key == "A":
        return cipher
    plain = ""
    back_shift_index = 26 - let_to_num(key)
    back_shift_key = num_to_let(back_shift_index)
    for char in cipher:
        plain += shift_char(char, back_shift_key)
    return plain


#############################################################
# Breaking the Caesar cipher
#############################################################

def letter_counts(s):
    counts = {char:0 for char in alpha}
    for char in s:
        counts[char] += 1
    return counts

def normalize(counts):
    total = 0
    for key in counts:
        total += counts[key]
    for key in counts:
        counts[key] /= total

# Uncomment the code below once the functions above are complete
english_freqs = letter_counts(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_freqs)

def distance(observed, expected):
    dist = 0
    sigma = lambda x: ((observed[x] - expected[x]) ** 2) / expected[x]
    for key in observed:
        dist += sigma(key)
    return dist

def caesar_break(cipher, frequencies): # rework this to use a dictionary and min()
    closest = None
    for key in alpha:
        contender = caesar_dec(cipher, key)
        counts = letter_counts(contender)
        normalize(counts)
        if closest is None or distance(counts, frequencies) < closest[2]:
            closest = [key, contender, distance(counts, frequencies)]
    return closest[:-1]

"""
hitchhiker = simplify_string(file_to_string("hitchhiker's.txt"))
hitchhiker_enc = caesar_enc(hitchhiker, "D")
string_to_file("hitchhiker_enc.txt", hitchhiker_enc)
cipher = simplify_string(file_to_string("hitchhiker_enc.txt"))
print(caesar_break(cipher, english_freqs)[1] == caesar_dec(cipher, "D"))

mystery1 = simplify_string(file_to_string("mystery1.txt"))
print(caesar_break(mystery1, english_freqs))
"""

#############################################################
# A working Vigenere cipher
#############################################################

def vigenere_enc(plain, key):
    cipher = ""
    i = 0
    for char in plain:
        if i >= len(key):
            i = 0
        cipher += shift_char(char, key[i])
        i += 1
    return cipher

def vigenere_dec(cipher, key):
    plain = ""
    i = 0
    for char in cipher:
        if i == len(key):
            i = 0
        if key[i] != "A":
            back_shift_index = 26 - let_to_num(key[i])
            back_shift_key = num_to_let(back_shift_index)
        else:
            back_shift_key = "A"
        plain += shift_char(char, back_shift_key)
        i += 1
    return plain


#############################################################
# Breaking the Vigenere cipher
#############################################################

def split_string(s, parts):
    split = ["" for i in range(parts)]
    i = 0
    for char in s:
        if i == parts:
            i = 0
        split[i] += char
        i += 1
    return split

def combine_split(split):
    s = ""
    length = len([j for i in range(len(split)) for j in split[i]])
    i = 0
    j = 0
    for n in range(length):
        if i == len(split):
            i = 0
            j += 1
        s += split[i][j]
        i += 1
    return s

def vig_break_for_length(cipher, klen, frequencies):
    letters = split_string(cipher, klen)
    key = ""
    for i in range(len(letters)):
        caesar = caesar_break(letters[i], frequencies)
        letters[i] = caesar[1]
        key += caesar[0]
    plain = combine_split(letters)
    return [key, plain]

def vig_break(c, maxlen, frequencies):
    contenders = {}
    for i in range(1, maxlen + 1):
        curr = vig_break_for_length(c, i, frequencies)
        counts = letter_counts(curr[1])
        normalize(counts)
        dist = distance(counts, frequencies)
        if dist in contenders:
            contenders[dist] = min(len(curr[1]), len(contenders[dist][1]))
        else:
            contenders[dist] = curr
    return contenders[min(contenders)]


"""
hitchhiker = simplify_string(file_to_string("hitchhiker's.txt"))
hitchhiker_enc = vigenere_enc(hitchhiker, "BAD")
string_to_file("hitchhiker_enc.txt", hitchhiker_enc)
cipher = simplify_string(file_to_string("hitchhiker_enc.txt"))
print(vig_break(cipher, 3, english_freqs)[1] == vigenere_dec(cipher, "BAD"))

mystery2 = simplify_string(file_to_string("mystery1.txt"))
print(vig_break(mystery2, 3, english_freqs))
"""


#############################################################
# A working substitution cipher
#############################################################

def sub_gen_key():
    alpha_list = list(alpha)
    random.shuffle(alpha_list)
    key = "".join(alpha_list)
    return key

def sub_enc(plain, key):
    cipher = ""
    for char in plain:
        index = alpha.index(char)
        cipher += key[index]
    return cipher

def sub_dec(cipher, key):
    plain = ""
    for char in cipher:
        index = key.index(char)
        plain += alpha[index]
    return plain

#############################################################
# Breaking the substitution cipher
#############################################################

def count_trigrams(s):
    counts = {}
    point1 = 0
    point2 = 3
    for i in range(len(s) - 2):
        tri = s[point1:point2]
        if tri in counts:
            counts[tri] += 1
        else:
            counts[tri] = 1
        point1 += 1
        point2 += 1
    return counts

# Uncomment the code below once the functions above are complete
english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_trigrams)

def map_log(d):
    for key in d:
        try:
            d[key] = log(d[key])
        except:
            d[key] == 0

# Uncomment the code below once the functions above are complete
map_log(english_trigrams)

def trigram_score(s, english_trigrams):
    trigrams = count_trigrams(s)
    score = 0
    for tri in trigrams:
        if tri in english_trigrams:
            score += english_trigrams[tri]
        else:
            score -= 15
    return score

def sub_break(cipher, english_trigrams):

    def rand_swap(key):
        key_list = list(key)
        letter1 = random.choice(key_list)
        index1 = key_list.index(letter1)
        while True:
            letter2 = random.choice(key_list)
            index2 = key_list.index(letter2)
            if letter2 != letter1:
                break
        key_list[index1] = letter2
        key_list[index2] = letter1
        return "".join(key_list)

    curr_key = sub_gen_key()
    cand_key = rand_swap(curr_key)
    score = lambda k: trigram_score(sub_dec(cipher, k), english_trigrams)
    i = 0
    while i <= 1000:
        if score(curr_key) < score(cand_key):
            i = 0
            curr_key = cand_key
            cand_key = rand_swap(curr_key)
        else:
            i += 1
    return [curr_key, sub_dec(cipher, curr_key)]


hitchhiker = simplify_string(file_to_string("hitchhiker's.txt"))
key = sub_gen_key()
hitchhiker_enc = sub_enc(hitchhiker, key)
string_to_file("hitchhiker_enc.txt", hitchhiker_enc)
cipher = simplify_string(file_to_string("hitchhiker_enc.txt"))
#print(sub_break(cipher, english_trigrams)[1])
print(sub_break(cipher, english_trigrams)[1] == sub_dec(cipher, key))

#mystery2 = simplify_string(file_to_string("mystery1.txt"))
#print(sub_break(mystery2, english_trigrams))
