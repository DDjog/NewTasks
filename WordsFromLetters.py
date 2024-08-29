import hunspell
# import enchant
from itertools import permutations
letters = ['a', 'c', 'e', 'i', 'l', 's', 'y', 'z', 'z']
aff_file = '/User/Dorota/Downloads/pl-dict.aff'
dic_file = '/User/Dorota/Downloads/pl-dict.dic'
#
hspell = hunspell.HunSpell(dic_file, aff_file)
# d = enchant.Dict("pl_PL")
#
# def find_words(hspell, letters):
"""
               Finding words from letters

               Parameters
               ----------
               args: ?, list
                     ?, list of letters

               Returns
               -------
               set of words and set of words with the length of 3 or 4 letters

               Examples
               --------
               Finding words from letters
               letters = ['a', 'c', 'e', 'i', 'l', 's', 'y', 'z', 'z']
               rslt=find_words(hspell, letters)
               print(rslt)
               ??
               """
#     words_list = set()
#     words_list_3_4 = set()
#
#     for length in range (2, len(letters)+1):
#         for perm in permutations(letters, length):
#             word = "".join(perm)
#             if hspell.check(word):
#                 words_list.add(word)
#                 if length == 3 or length ==4:
#                     words_list_3_4.add(word)
#
#     return words_list, words_list_3_4
#
#
# rslt = find_words(hspell, letters)
# print(rslt)

import os


hunspell_dirs = [
    "/usr/share/hunspell",
    "/usr/local/share/hunspell",
    "/Library/Spelling",
    "C://Program Files//Hunspell//Dictionaries"
]


available_languages = []


for directory in hunspell_dirs:
    if os.path.exists(directory):
        for filename in os.listdir(directory):
            if filename.endswith(".dic"):
                language = filename.split('.')[0]
                available_languages.append(language)


print("Dostępne słowniki hunspell:")
for language in available_languages:
    print(language)


if 'pl_PL' in available_languages:
    print("\nSłownik polski (pl_PL) jest dostępny.")
else:
    print("\nSłownik polski (pl_PL) nie jest dostępny.")

print(hspell.spell("przykład"))


