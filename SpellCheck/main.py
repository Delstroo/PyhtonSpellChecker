import re
import tkinter as tk
from tkinter import scrolledtext

import nltk
from nltk.corpus import words

nltk.download("words")

class SpellingChecker:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("800x400")  # Adjusted window size

        self.text = scrolledtext.ScrolledText(self.root, font=("Arial", 14))
        self.text.bind("<KeyRelease>", lambda event=None: self.check(event))
        self.text.pack(expand=True, fill="both")  # Adjusted widget settings
 
        self.old_oldspaces = 0

        self.root.mainloop()


    def check(self, event):
        content = self.text.get("1.0", tk.END)
        space_count = content.count(" ")

        if space_count != self.old_oldspaces:
            self.old_oldspaces = space_count
        
            for tag in self.text.tag_names():
                self.text.tag_delete(tag)
            
            for word in content.split(" "):
                if re.sub(r"[^\w]", "", word.lower()) not in words.words():
                    position = content.find(word)
                    self.text.tag_add(word, f"1.{position}", f"1.{position + len(word)}")
                    self.text.tag_config(word, foreground="red")


SpellingChecker()