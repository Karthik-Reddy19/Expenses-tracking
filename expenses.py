class Expense:
    def __init__(self,amount,category,date):
        self.amount=amount
        self.category=category
        self.date=date
expenses=[]
def load_from_file():
    try:
        with open("expenses.txt", "r") as f:
            for line in f:
                amount, category, date = line.strip().split(",")
                exp = Expense(int(amount), category, date)
                expenses.append(exp)
    except FileNotFoundError:
        pass
def save_to_file():
    with open("expenses.txt", "w") as f:
        for i in expenses:
            f.write(f"{i.amount},{i.category},{i.date}\n")

def add_expense():
    amount=int(input("Enter the amount:"))
    category=input("Enter the category:")
    date=input("Enter the date:")
    exp=Expense(amount,category,date)
    expenses.append(exp)
    save_to_file()
    print("Expense added successfully")
def view_expenses():
    if not  expenses:
        print("no expenses found")
        return
    for i in expenses:
        print("Amount",i.amount,"Category",i.category,"date",i.date)

def total():
    total=0
    for i in expenses:
        total+=i.amount
    print("Total Expenses:",total)
def search():
    cat=input("Enter the category")
    found=False
    for i in expenses:
        if i.category==cat:
            print("Amount",i.amount,"Category",i.category,"date",i.date)
            found=True
    if not found:
        print("No matching expenses")
def delete_expense():
    cat=input("Enter the category")
    for i in expenses:
        if i.category==cat:
            expenses.remove(i)
            print("Deleted successfully")
            return
    print("Expenses not found")
load_from_file()
while True:
    print("MENU\n")
    print("1.Add \n2.View\n3.Total\n4.Search\n5.Delete\n6.Exit")
    choice=int(input("Enter your choice::"))
    if choice == 1:
        add_expense()
    elif choice == 2:
        view_expenses()
    elif choice == 3:
        total()
    elif choice == 4:
        search()
    elif choice == 5:
        delete_expense()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
