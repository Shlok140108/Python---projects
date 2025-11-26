import tkinter as tk
from tkinter import messagebox
from library import Book, Library

library = Library("storage.csv")

root = tk.Tk()
root.title("Python Library System")
root.geometry("450x400")
root.config(bg="#e6f2ff")

# Input Labels & Boxes
tk.Label(root, text="Book Title:", bg="#e6f2ff").pack()
title_entry = tk.Entry(root, width=30)
title_entry.pack(pady=5)

tk.Label(root, text="Author:", bg="#e6f2ff").pack()
author_entry = tk.Entry(root, width=30)
author_entry.pack(pady=5)

tk.Label(root, text="Price:", bg="#e6f2ff").pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack(pady=5)

# Functions connected to backend
def add_book_gui():
    title = title_entry.get()
    author = author_entry.get()
    price = price_entry.get()
    if not title or not author or not price:
        messagebox.showerror("Error", "All fields required!")
        return
    
    library.add_book(Book(title, author, price))
    messagebox.showinfo("Success", "Book Added Successfully!")

def search_book_gui():
    title = title_entry.get()
    result = library.search_book(title)
    if result:
        messagebox.showinfo("Found", result)
    else:
        messagebox.showinfo("Not Found", "Book does not exist.")

def remove_book_gui():
    title = title_entry.get()
    if library.remove_book(title):
        messagebox.showinfo("Removed", "Book Deleted Successfully!")
    else:
        messagebox.showwarning("Error", "Book Not Found!")

# Buttons
tk.Button(root, text="Add Book", command=add_book_gui).pack(pady=8)
tk.Button(root, text="Search Book", command=search_book_gui).pack(pady=8)
tk.Button(root, text="Remove Book", command=remove_book_gui).pack(pady=8)

root.mainloop()
