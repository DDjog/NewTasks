import hunspell
from itertools import permutations
letters = ['a', 'c', 'e', 'i', 'l', 's', 'y', 'z', 'z']
aff_file = '/User/Dorota/Downloads/pl-dict.aff'
dic_file = '/User/Dorota/Downloads/pl-dict.dic'
#
hspell = hunspell.HunSpell(dic_file, aff_file)

#
def find_words(hspell, letters):
    """
               Finding words from letters

               Parameters
               ----------
               args: instance of a dictionary, list
                     polish dictionary, list of letters

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
    words_list = set()
    words_list_3_4 = set()

    for length in range (2, len(letters)+1):
        for perm in permutations(letters, length):
            word = "".join(perm)
            if hspell.check(word):
                words_list.add(word)
                if length == 3 or length ==4:
                    words_list_3_4.add(word)

    return words_list, words_list_3_4
#
#
rslt = find_words(hspell, letters)
print(rslt)



