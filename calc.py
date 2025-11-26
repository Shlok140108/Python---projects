class Calculator:
    def __init__(self):
        self.history = []
    
    def calculate(self, exp):
        try:
            result = eval(exp)

            record = f"{exp} = {result}"
            self.history.append(record)

            with open("HistoryForCalc.csv", "a") as file:
                file.write(record + "\n")

            return result
        
        except ValueError:
            print("Uh Ohh.. I think you messed up while using me... Invalid Input.... Please Try Again...!!!")

        
    def show_history(self):
        if not self.history:
            print("No Calculation yet")
        else:
            print("<<------Calculation History------>>")
            for entry in self.history:
                print(entry)
            print("<<------------------------------->>")

def main():
    calc = Calculator()
    print("Welcome to my Own Build Calculator")
    print("<<<<<---------------------------------------------------------------->>>>>")

    while True:
        exp = input("Enter the Expression(e.g 5 + 2) or 'h' for history or 'q' to quit: ").lower()

        if exp == "q":
            print("Thanks!!! For using me... GoodBye...")
            break

        elif exp == "h":
            calc.show_history()
            continue

        result = calc.calculate(exp)
        print(f"Result = {result}")


if __name__ == "__main__":
    main()

            
