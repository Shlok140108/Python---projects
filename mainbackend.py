import csv
import os
import time
import sys

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
                    print(f"BOOK FOUND!!! {row[0]} by {row[1]} is of ${row[2]}")
                    found = True
                    return

        if not found:           
            print("BOOK NOT FOUND")

    def view_book(self):
        with open("storage.csv" , "r") as file:
            reader = csv.reader(file)
            next(reader)

            found = False 
            for row in reader:
                found = True
                
                print(f"Title: {row[0]} , Author: {row[1]} , Price: ${row[2]}")

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
            with open("storage.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            loading_animation("Removing Book")
            print (f"Book {title} Removed Successfully!!")
        
        else:
            print()


       
def main():
    library = Library("storage.csv")

    while True:
        time.sleep(2)
        print("<<<<<<------Welcome to the Python Library------>>>>>>")
        print("1.Add a book")
        print("2.Search a book")
        print("3.View Books")
        print("4.Remove book")
        print("5.Exit")
        

        choice = input("Enter a option number from above choices: ")

        if choice == "1":
            title = input("Title of the Book: ")
            author = input("Author of the Book: ")
            price = input("Price of the Book: ")
            library.add_book(Book(title,author,price))
        

        elif choice == "2":
            title = input("Enter the book title: ")
            library.search_book(title)


        elif choice == "3":
            library.view_book()

        elif choice == "4":
            title  = input("Enter the book title: ")
            library.remove_book(title)

        elif choice == "5":
            loading_animation("Thanks for visiting")
            break

        else:
            print("INCORRECT Choice... Please Try Again...")

if __name__ == "__main__":
    main()


