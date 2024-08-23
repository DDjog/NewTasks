import enchant
from itertools import permutations
letters = ['a', 'c', 'e', 'i', 'l', 's', 'y', 'z', 'z']
d = enchant.Dict("en_US")


def find_words(d, letters):
    words_list = set()

    for length in range (2, len(letters)+1):
        for perm in permutations(letters, length):
            word = "".join(perm)
            if d.check(word):
                words_list.add(word)

    return words_list


rslt = find_words(d, letters)
print(rslt)




# def find_word(d, letters):
#     words_list = []
#     letters_copy = letters.copy()
#
#     for word in d:
#         for l in word:
#             if l in letters_copy:
#                 letters_copy.remove(l)
#             else:
#                 break
#         else:
#             words_list.append(word)
#
#     return words_list
#
# 
# rslt = find_word(d, letters)
# print(rslt)