from spellchecker import SpellChecker
from itertools import permutations
letters = ['a', 'c', 'e', 'i', 'l', 's', 'y', 'z', 'z']
spell = SpellChecker()


def find_words(spell, letters):
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
               rslt=find_words(spell, letters)
               print(rslt)
               ??
               """
    words_list = set()
    words_list_3_4 = set()

    for length in range (2, len(letters)+1):
        for perm in permutations(letters, length):
            word = "".join(perm)
            if spell.unknown([word])==set():
                words_list.add(word)
                if length == 3 or length ==4:
                    words_list_3_4.add(word)
    return words_list


rslt = find_words(spell, letters)
print(rslt)

string = "one,two,three"
words = string.split(',')
print(words)