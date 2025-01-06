from tkinter import *
from itertools import permutations
from spellchecker import SpellChecker

root = Tk()
root.title('Words from letters')

spell = SpellChecker()

def comma_window():
    comma_window = Toplevel()
    comma_window.title('Attention')

    text_comma_window = Label(comma_window, text='Letters should be separated with comma', fg='red')
    text_comma_window.grid(row=0, column=1, sticky='ew', padx=10, pady=10)

    button_quit_comma_window = Button(comma_window, text='Ok', command=comma_window.destroy)
    button_quit_comma_window.grid(row=5, column=1, columnspan=2, sticky='e', padx=10, pady=10)

def root_configuration():
    global text_list
    global e
    root.rowconfigure(0, weight=10)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=10)
    root.rowconfigure(3, weight=1)
    root.rowconfigure(4, weight=1)
    root.rowconfigure(5, weight=1)
    root.columnconfigure(0, weight=5)
    root.columnconfigure(1, weight=1)

    e = Entry(root, width=50)
    e.grid(row=1, column=0, padx=10, pady=10)

    e_label = Label(root, text='Enter letters separated with comma (e.g.: a,d,t)')
    e_label.grid(row=0, column=0, sticky='ew', padx=10, pady=10)

    add_in_e = Button(root, text='Click here to generate words', command=generate_words, fg='blue')
    add_in_e.grid(row=2, column=0, sticky='ew', padx=10, pady=10)

    text_list_label = Label(root, text='List of generated words:')
    text_list_label.grid(row=3, column=0, columnspan=2, sticky='w', padx=10, pady=5)

    text_list = Listbox(root, width=60, height=15)
    text_list.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

    button_copy_to_clipboard = Button(root, text='Copy to clipboard', command=gtc)
    button_copy_to_clipboard.grid(row=5, column=0, sticky='e', padx=10, pady=10)

    button_quit = Button(root, text='Close', command=root.destroy)
    button_quit.grid(row=5, column=1, columnspan=2, sticky='e', padx=10, pady=10)

def generate_words():
    text = e.get()
    letters = text.split(',')
    if ',' not in text:
        comma_window()
        e.delete(0,END)
        return
    else:
        words_list = set()

        for length in range(2, len(letters) + 1):
            for perm in permutations(letters, length):
                word = "".join(perm)
                if spell.unknown([word]) == set():
                    words_list.add(word)

        text_list.delete(0, END)
        for word in sorted(words_list):
            text_list.insert(END, word)

def gtc():
    text=text_list.get(0, END)
    if text:
        root.clipboard_clear()
        root.clipboard_append(text)
        print('List of words copied to clipboard')
    else:
        print('No words to be copied to clipboard')

root_configuration()
root.mainloop()