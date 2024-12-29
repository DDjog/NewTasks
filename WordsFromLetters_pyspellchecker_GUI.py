from tkinter import *
from itertools import permutations
from spellchecker import SpellChecker

root = Tk()
root.title('Words from letters')

root.rowconfigure(0, weight=10)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=10)
root.rowconfigure(3, weight=1)
root.columnconfigure(0, weight=5)
root.columnconfigure(1, weight=1)

e = Entry(root, width=50)
e.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

spell = SpellChecker()

def generate_words():
    text = e.get()
    letters = text.split(',')
    words_list = set()

    for length in range(2, len(letters) + 1):
        for perm in permutations(letters, length):
            word = "".join(perm)
            if spell.unknown([word]) == set():
                words_list.add(word)

    text_list.delete(0, END)
    for word in sorted(words_list):
        text_list.insert(END, word)

add_in_e = Button(root, text='Generate words', command=generate_words)
add_in_e.grid(row=1, column=0, sticky='ew', padx=10, pady=10)

text_list_label = Label(root, text='List of generated words:')
text_list_label.grid(row=2, column=0, columnspan=2, sticky='w', padx=10, pady=5)

text_list = Listbox(root, width=60, height=15)
text_list.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

button_quit = Button(root, text='Close', command=root.destroy)
button_quit.grid(row=4, column=0, columnspan=2, sticky='e', padx=10, pady=10)

root.mainloop()
