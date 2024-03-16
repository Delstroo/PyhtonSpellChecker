import re
import tkinter as tk
from tkinter import scrolledtext

import nltk
from nltk.corpus import words as nltk_words

nltk.download("words")

class SpellingChecker:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x400")

        self.text = scrolledtext.ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", self.check_word)
        self.text.pack(expand=True, fill="both")
 
        self.english_words = set(nltk_words.words())
        self.old_text = ""

        self.root.mainloop()

    def check_word(self, event):
        new_text = self.text.get("1.0", tk.END)

        if new_text != self.old_text:
            changed_text = new_text[len(self.old_text):]
            words_to_check = re.findall(r'\b\w+\b', changed_text)

            for word in words_to_check:
                if word.lower() not in self.english_words:
                    start_index = new_text.find(word)
                    end_index = start_index + len(word)
                    self.text.tag_add(word, f"1.{start_index}", f"1.{end_index}")
                    self.text.tag_config(word, foreground="red")

        self.old_text = new_text


SpellingChecker()
