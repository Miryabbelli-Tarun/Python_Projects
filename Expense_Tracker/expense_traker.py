import sqlite3
from datetime import datetime
import csv

DATABASE=("expense.db")
def get_connection():
    return sqlite3.connect(DATABASE)

def init_database():
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS expenses(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                note TEXT,
                date TEXT NOT NULL
            )
        """)
        conn.commit()

def add_expense():
    print("\n_____Add Expenses_______")
    try:
        amount=float(input("Enter amount:"))
    except ValueError:
        print("Enter valid amount")
        return
    category=input("Enter category(food/travel/shopping/etc..):")
    note=input("Enter description(optional):").strip()
    today=datetime.now().strftime("%Y-%m-%d")

    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "INSERT INTO expenses (amount,category,note,date) VALUES (?,?,?,?)",(amount,category,note,today)
        )
        conn.commit()
        print("\n Expenses enter sucesfully\n")

def view_expenses():
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT ID,amount,category,note,date FROM expenses"
        )
        rows=cursor.fetchall()

        if not rows:
            print("no result found")
            return
        for row in rows:
            ID,amount,category,note,date=row
            print(f"ID: {ID} | ₹{amount} | {category} | {note} | {date}")
    print("-------------\n")

def view_by_category():
    category=input("Enter category to view Expenses(food/travel/shopping/etc..):")
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "select ID,amount,category,note,date FROM expenses where category=? order by date DESC",(category,)

        )
        rows=cursor.fetchall()

        if not rows:
            print("no result found in category")
            return
        for row in rows:
            ID,amount,category,note,date=row
            print(f"ID: {ID} | ₹{amount} | {category} | {note} | {date}")
    print("-------------\n")

def view_by_date_range():
    print("\n view expenses by enter date in formate(yy-mm-dd)")
    start_date=input("Enter start date:")
    end_date=input("Enter ending date:")
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "select ID,amount,category,note,date from expenses where date BETWEEN ?AND ? order by date DESC",(start_date,end_date)

        )
        rows=cursor.fetchall()
        print(f"Expenses between {start_date} and {end_date}")
        if not rows:
            print("no result found in date range")
            return
        for row in rows:
            ID,amount,category,note,date=row
            print(f"ID: {ID} | ₹{amount} | {category} | {note} | {date}")
    print("-------------\n")

def show_monthly_total():
    print("Show monthly total Expenses")
    current_month = datetime.now().strftime("%Y-%m")
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT SUM(amount) FROM expenses
            WHERE date LIKE ?
        """, (current_month + "%",))
        row = cursor.fetchone()
        total = row[0] if row[0] is not None else 0

    print(f"\nTotal spent this month ({current_month}): ₹{total}\n")

def show_max_expense():
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT ID, amount, category, note, date FROM expenses ORDER BY amount DESC LIMIT 1"
        )
        row=cursor.fetchone()

        if not row:
            print("no expenses found")
            return
        ID,amount,category,note,date=row
        print(f"Maximum expense is")
        print(f"ID: {ID} | ₹{amount} | {category} | {note} | {date}")

def delete_expenses():
    try:
        exp_id=int(input("Enter expense id to delete:"))
    except ValueError:
        print("Enter valid id")
        return
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT ID,amount,category,note,date FROM expenses WHERE ID=?",(exp_id,)
        )
        row=cursor.fetchone()

        if not row:
            print("no expense found with ID")
            return
        
        ID,amount,category,note,date=row
        print(f"ID: {ID} | ₹{amount} | {category} | {note} | {date}")
        option=input("are you sure to delete the expense(y/n):").lower()
        if option=="y":
            cursor.execute(
                "DELETE FROM expenses WHERE ID=?",(exp_id,)
            )
            conn.commit()
            print("delete sucesfully")
        else:
            print("Delete canceled..")

def update_expenses():
    try:
        exp_id=int(input("Enter expence id to edit:"))
    except ValueError:
        print("Enter valid id ")
        return     
    
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT ID,amount,category,note,date FROM expenses WHERE ID=?",(exp_id,)
        )
        row=cursor.fetchone()

        if not row:
            print("No expense found")
            return
        
        ID,old_amount,old_category,old_note,old_date=row
        print(f"Current: ID:{ID} | ₹{old_amount} | {old_category} | {old_note} | {old_date}")

        new_amount=input("Enter new amount or(press Enter to keep old amount):").strip()
        new_category=input("Enter new category or(Press enter to keep old category):").strip()
        new_note=input("Enter new note or(Press enter to keep old note):").strip()
        new_date=input("Enter new date or (Press enter to keep old date):").strip()

        try:
            amount_input=float(new_amount) if new_amount else old_amount
        except ValueError:
            print("Invalid new amount,so keep old amount")
            amount_input=new_amount
        category_input=new_category if new_category else old_category
        note_input=new_note if new_note else old_note
        date_input=new_date if new_date else old_date

        cursor.execute(
            "UPDATE expenses SET amount=? ,category=?,note=?,date=? WHERE ID=?",(amount_input,category_input,note_input,date_input,exp_id)
        )
        conn.commit()
        print("Update succesful...")

def get_category_wise_total_amount():
    print("--------category wise total amount-------------")
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT category,SUM(amount) as total FROM expenses GROUP BY category ORDER BY total DESC"
        )
        rows=cursor.fetchall()

        if not rows:
            print("No expenses found!!!")
        category,total=rows
        for category,total in rows:
            print(f"{category}  : ₹{total}")

def search_by_note_keyword():
    keyword=input("Enter note/description keyword to search:").strip()

    if not keyword:
        print("Invalid keyword")
        return
    
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT ID,amount,category,note,date FROM expenses WHERE NOTE LIKE ? ORDER BY date DESC",(f"%{keyword}%",)
        )
        rows=cursor.fetchall()

        if not rows:
            print("no expenses found")
            return
        for row in rows:
            ID,amount,category,note,date=row
            print(f"ID: {ID} | ₹{amount} | {category} | {note} | {date}")

def download_expenses_csv():
    file_name="expenses_csv.csv"

    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT ID,amount,category,note,date FROM expenses ORDER BY date DESC"
        )
        rows=cursor.fetchall()

        if not rows:
            print("No expenses found")
            return
        
        with open(file_name,"w",newline="\n") as file:
            writer=csv.writer(file)

            writer.writerow(["ID", "Amount", "Category", "Note", "Date"])
            writer.writerows(rows)

    print("CSV file download successfully...")

        

        
def main_menu():
    init_database()

    while True:
        print("\n---------Expense traker-----------------\n")
        print("1.Add expenses")
        print("2.view expenses")
        print("3.view expenses by category")
        print("4.View expenses by date range")
        print("5.show total spent on this month")
        print("6.Show highest expense")
        print("7.edit expenses")
        print("8.Delete")
        print("9.Get category wise total amount")
        print("10.Search by note keyword")
        print("11.Download csv file")
        print("0.exit")
        choice=input("\n Enter number to select one service: ")
        
        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expenses()
        elif choice=="3":
            view_by_category()
        elif choice=="4":
            
            view_by_date_range()
        elif choice=="5":
            
            show_monthly_total()
        elif choice=="6":          
            show_max_expense()
        elif choice=="7":
            update_expenses()
        elif choice=="8":
            
            delete_expenses()
        elif choice=="9":
            get_category_wise_total_amount()
        elif choice=="10":
            search_by_note_keyword()
        elif choice=="11":
            download_expenses_csv()
        elif choice=="0":
            print("Exite....")
            break
        else:
            print("Enter valid choice")

if __name__=="__main__":
    main_menu()    
