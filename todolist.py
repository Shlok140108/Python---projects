tasks = []

def add_task(title):
    tasks.append({"title": title , "done" : False})
    print("Tasks Added")

def show_tasks():
    if not tasks:
        print("No tasks yet!!")
        return 
    
    print("\n-----Your Tasks-----")
    num = 1
    for item in tasks:
        status = "✔️" if item["done"] else "❌"
        print(f"{num}. {item["title"]} {[status]}")
        num += 1

def delete_task(title):
    for item in tasks:
        if item["title"].lower() == title.lower():
            tasks.remove(item)
            print(f"Task {title} Removed")
            return
        
    print("Task Not Found!!")

def mark_done(title):
    for item in tasks:
        if item["title"].lower() == title.lower():
            item["done"] = True
            print(f"Task {title} marked as done...")
            return
    
    print("Task Not Found!!")

def main():
    while True:
        print("<<<<------ TO DO MENU ------>>>>")
        print("1. ADD TASK")
        print("2. SHOW TASK")
        print("3. MARK A TASK AS DONE")
        print("4. DELETE A TASK")
        print("5. EXIT")

        choice = input("Choose: ")

        if choice == "1":
            title = input("Task Name: ")
            add_task(title)

        elif choice == "2":
            show_tasks()

        elif choice == "3":
            title = input("Task name: ")
            mark_done(title)

        elif choice == "4":
            title = input("Task name: ")
            delete_task(title)

        elif choice == "5":
            print("Thanks For Visiting")
            break

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()