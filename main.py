import tkinter as tk
from tkinter import messagebox

class GameApp:
    def __init__(self, master):
        self.master = master
        master.title("Game of Words")

        self.label = tk.Label(master, text="Введите слово:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.check_button = tk.Button(master, text="Проверить", command=self.check_word)
        self.check_button.pack()

        self.words_label = tk.Label(master, text="Последние 10 слов:")
        self.words_label.pack()

        self.words = ["", ""]
        self.word_list = []
        self.listbox = tk.Listbox(master, height=10)
        self.listbox.pack()

    def check_word(self):
        word = self.entry.get().lower()

        if len(word) == 0:
            messagebox.showwarning("Не правильное слово", "Пожалуйста, введите слово")
        elif self.words[1] != "" and self.words[1][-1].lower() != word[0]:
            messagebox.showinfo("Первая буква вашего слова не совпадает с последней предыдущего.\n\nGame over!")
            self.master.destroy()
        else:
            self.words[0], self.words[1] = self.words[1], word
            self.words_label.config(text="Последнее слово: " + " ".join(self.words[1]))
            self.entry.delete(0, tk.END)
            self.word_list.append(word)
            self.listbox.insert(tk.END, word)

            if len(self.word_list) > 10:
                self.listbox.delete(0)
                self.word_list.pop(0)

root = tk.Tk()
app = GameApp(root)
root.mainloop()
