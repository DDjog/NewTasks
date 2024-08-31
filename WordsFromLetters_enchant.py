import enchant
from itertools import permutations
letters = ['a', 'c', 'e', 'i', 'l', 's', 'y', 'z', 'z']
d = enchant.Dict("pl_PL")
#
def find_words(d, letters):
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
               rslt=find_words(d, letters)
               print(rslt)
               ??
               """
    words_list = set()
    words_list_3_4 = set()

    for length in range (2, len(letters)+1):
        for perm in permutations(letters, length):
            word = "".join(perm)
            if d.check(word):
                words_list.add(word)
                if length == 3 or length ==4:
                    words_list_3_4.add(word)

    return words_list, words_list_3_4


rslt = find_words(d, letters)
print(rslt)