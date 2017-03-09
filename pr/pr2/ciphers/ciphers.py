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

# creates list comprehension of the char.upper() for char in string,
# if char in alpha. returns string of list using "".join()
def simplify_string(s):
    ls = [char.upper() for char in s if char.upper() in alpha]
    return "".join(ls)

# returns letter at index x of alpha
def num_to_let(x):
    return alpha[x]

# returns the index of alpha containing a.upper()
def let_to_num(a):
    return alpha.index(a.upper())

# uses let_to_num() and num_to_let() to shifted index of alpha
# impliments wrap-around if necessary
def shift_char(char, shift):
    char_index = let_to_num(char)
    shift_index = let_to_num(shift)
    out_index = char_index + shift_index
    if out_index >= 26:
        out_index = out_index - 26
    return alpha[out_index]

# simply applies shift_char() to each letter in plain using key as shift
def caesar_enc(plain, key):
    cipher = ""
    for char in plain:
        cipher += shift_char(char, key)
    return cipher

# uses a computed back_shift to use same process as caesar_enc()
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

# creates a dictionary containing the counts of each char in s
def letter_counts(s):
    counts = {char:0 for char in alpha}
    for char in s:
        counts[char] += 1
    return counts

# normalizes a counts dict
def normalize(counts):
    total = 0
    for key in counts:
        total += counts[key]
    for key in counts:
        counts[key] /= total

english_freqs = letter_counts(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_freqs)

# impliments sigma algorithm as a lambda function
# returns the distance accordingly
def distance(observed, expected):
    dist = 0
    sigma = lambda x: ((observed[x] - expected[x]) ** 2) / expected[x]
    for key in observed:
        dist += sigma(key)
    return dist

# attempts caesar_dec() on cipher with each key in alpha
# keeps track of which contender has so far been the closest,
# and returns it accordingly
def caesar_break(cipher, frequencies):
    closest = None
    for key in alpha:
        contender = caesar_dec(cipher, key)
        counts = letter_counts(contender)
        normalize(counts)
        if closest is None or distance(counts, frequencies) < closest[2]:
            closest = [key, contender, distance(counts, frequencies)]
    return closest[:-1]

#below checks caesar_break
"""
hitchhiker = simplify_string(file_to_string("hitchhiker's.txt"))
hitchhiker_enc = caesar_enc(hitchhiker, "D")
string_to_file("hitchhiker_enc.txt", hitchhiker_enc)
cipher = simplify_string(file_to_string("hitchhiker_enc.txt"))
print(caesar_break(cipher, english_freqs)[1] == caesar_dec(cipher, "D"))
"""

#############################################################
# A working Vigenere cipher
#############################################################

# cycles through each char in key and applies shift_char() to char in plain accordingly
def vigenere_enc(plain, key):
    cipher = ""
    i = 0
    for char in plain:
        if i >= len(key):
            i = 0
        cipher += shift_char(char, key[i])
        i += 1
    return cipher

# uses same cycling behavior from vig_enc() and back_shift() from caesar_dec()
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

# creates a list of empty strings for each part
# cycles through i, like above,
# and adds each char in s to the corresponding string in split
def split_string(s, parts):
    split = ["" for i in range(parts)]
    i = 0
    for char in s:
        if i == parts:
            i = 0
        split[i] += char
        i += 1
    return split

# uses cycling behavior to reverse a split list from split_string()
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

# applies caesar_break for each key in alpha for a given cipher and keylen
# returns [key, plain]
def vig_break_for_length(cipher, klen, frequencies):
    letters = split_string(cipher, klen)
    key = ""
    for i in range(len(letters)):
        caesar = caesar_break(letters[i], frequencies)
        letters[i] = caesar[1]
        key += caesar[0]
    plain = combine_split(letters)
    return [key, plain]

# applies vig_break_for_length() for each possible length up to the maxlen
# stores contenders in a dict and pops min when done
# returns [key, plain]
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
    return contenders.pop(min(contenders))

#below checks vig_break
"""
hitchhiker = simplify_string(file_to_string("hitchhiker's.txt"))
hitchhiker_enc = vigenere_enc(hitchhiker, "BAD")
string_to_file("hitchhiker_enc.txt", hitchhiker_enc)
cipher = simplify_string(file_to_string("hitchhiker_enc.txt"))
print(vig_break(cipher, 3, english_freqs)[1] == vigenere_dec(cipher, "BAD"))
"""

#############################################################
# A working substitution cipher
#############################################################

# creates list of alpha and shuffles
# returns string of shuffled list using "".join()
def sub_gen_key():
    alpha_list = list(alpha)
    random.shuffle(alpha_list)
    key = "".join(alpha_list)
    return key

# takes index of each plain char in alpha,
# and adds to the cipher that index in the key
def sub_enc(plain, key):
    cipher = ""
    for char in plain:
        index = alpha.index(char)
        cipher += key[index]
    return cipher

# does the opposite of sub_enc()
def sub_dec(cipher, key):
    plain = ""
    for char in cipher:
        index = key.index(char)
        plain += alpha[index]
    return plain

#############################################################
# Breaking the substitution cipher
#############################################################

# impliments two pointers that move across the string in sync
# adds each corresponding trigram (the chars between the pointers) to the dict
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

english_trigrams = count_trigrams(simplify_string(file_to_string("twocities_full.txt")))
normalize(english_trigrams)

# uses a try/except to apply math.log() to each value in the trigram dict
def map_log(d):
    for key in d:
        try:
            d[key] = log(d[key])
        except:
            d[key] == 0

map_log(english_trigrams)

# computes trigram_score of string using a scored trigram dict (eg. english_trigrams)
def trigram_score(s, english_trigrams):
    trigrams = count_trigrams(s)
    score = 0
    for tri in trigrams:
        if tri in english_trigrams:
            score += english_trigrams[tri]
        else:
            score -= 15
    return score

# literally works 99% of the time... not sure if that's acceptable or not.
# uses rand_swap() to impliment algorithm outlined in the project.pdf
# simple while loop
# makes use of a lambda that computes trigram scores for sake of brevity
def sub_break(cipher, english_trigrams):

    # uses list() and "".join() to randomly select a letter from the key
    # and switches it with another random letter
    # uses a while True loop to ensure that it does not swap the same letters
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
    score = lambda k: trigram_score(sub_dec(cipher, k), english_trigrams)
    i = 0
    while i <= 1000:
        cand_key = rand_swap(curr_key)
        if score(curr_key) < score(cand_key):
            i = 0
            curr_key = cand_key
            cand_key = rand_swap(curr_key)
        else:
            i += 1

    return [curr_key, sub_dec(cipher, curr_key)]

#below checks sub_break
"""
hitchhiker = simplify_string(file_to_string("hitchhiker's.txt"))
key = "JZMSKIRLPWVNUEXDTCGYFQBHOA"
hitchhiker_enc = sub_enc(hitchhiker, key)
string_to_file("hitchhiker_enc.txt", hitchhiker_enc)
cipher = simplify_string(file_to_string("hitchhiker_enc.txt"))
"""

#below decrypts mysteries 1, 2, 3
"""
mystery1 = simplify_string(file_to_string("mystery1.txt"))
string_to_file("myster1_dec.txt", caesar_break(mystery1, english_freqs)[1])

mystery2 = simplify_string(file_to_string("mystery2.txt"))
string_to_file("mystery2_dec.txt", vig_break(mystery2, 3, english_freqs)[1])

mystery3 = simplify_string(file_to_string("mystery3.txt"))
string_to_file("mystery2_dec.txt", sub_break(mystery2, english_trigrams)[1])
"""
