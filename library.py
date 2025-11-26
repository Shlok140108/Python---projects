import csv
import os
import time
import sys
import tkinter as tk
from tkinter import messagebox


def loading_animation(message="Processing"):
    for i in range(4):  
        sys.stdout.write("\r" + message + "." * (i + 1))  
        sys.stdout.flush()
        time.sleep(0.5)
    print() 

class Book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def list(self):
        return [self.title , self.author , self.price]
    
class Library:
    def __init__(self,storage):
        self.storage = storage 

        if not os.path.exists("storage.csv"):
            with open("storage.csv", "w" , newline = "") as file:
                writer = csv.writer(file)
                writer.writerow(["Title" , "Author" , "Price"])

    def add_book(self,book):
        with open ("storage.csv" , "a" , newline = "") as file:
            writer = csv.writer(file)
            writer.writerow(book.list())
        
        loading_animation("Adding Book")
        print(f"Book '{book.title}' added succesfully")

    def search_book(self,title):
        with open ("storage.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                if row[0].lower() == title.lower():
                    loading_animation("Finding Book")
                    return f"BOOK FOUND!!! {row[0]} by {row[1]} is of ${row[2]}"
                    
        return None

    def view_book(self):
        books = []
        with open ("storage.csv" , "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                books.append(row)
        
        return books
    
    def remove_book(self,title):
        rows = []
        removed = False

        with open("storage.csv" , "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0].lower() == title.lower():
                    removed = True
                    continue 
                rows.append(row)

        if removed:
            with open(self.storage, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            return f"Book '{title}' removed successfully!"
        else:
            return None

       

class LibraryGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Library System")

        self.library = Library("storage.csv")

        # Labels + Entry fields
        tk.Label(root, text="Title:").grid(row=0, column=0)
        tk.Label(root, text="Author:").grid(row=1, column=0)
        tk.Label(root, text="Price:").grid(row=2, column=0)

        self.title_entry = tk.Entry(root)
        self.author_entry = tk.Entry(root)
        self.price_entry = tk.Entry(root)

        self.title_entry.grid(row=0, column=1)
        self.author_entry.grid(row=1, column=1)
        self.price_entry.grid(row=2, column=1)

        # Buttons
        tk.Button(root, text="Add Book", command=self.add_book_gui).grid(row=3, column=0)
        tk.Button(root, text="Search Book", command=self.search_book_gui).grid(row=3, column=1)
        tk.Button(root, text="View Book", command=self.view_book_gui).grid(row=4, column=0)
        tk.Button(root, text="Remove Book", command=self.remove_book_gui).grid(row=4, column=1)

    def add_book_gui(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        price = self.price_entry.get()
        message = self.library.add_book(Book(title, author, price))
        messagebox.showinfo("Success", message)

    def search_book_gui(self):
        title = self.title_entry.get()
        result = self.library.search_book(title)
        if result:
            messagebox.showinfo("Book Found", result)
        else:
            messagebox.showerror("Not Found", "Book not found!")

    def remove_book_gui(self):
        title = self.title_entry.get()
        result = self.library.remove_book(title)
        if result:
            messagebox.showinfo("Removed", result)
        else:
            messagebox.showerror("Not Found", "Book not found!")

    def view_book_gui(self):
        books = self.library.view_book()
        if books:
            message = "\n".join([f"{b[0]} by {b[1]} (${b[2]})" for b in books])
            messagebox.showinfo("All Books", message)
        else:
            messagebox.showinfo("Empty", "No books available!")


if __name__ == "__main__":
    root = tk.Tk()
    gui = LibraryGUI(root)
    root.mainloop()

