import sqlite3

DB_NAME="student.db"
def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Student(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                rollno INTEGER UNIQUE,
                branch TEXT ,
                marks REAL
                )
""")
        conn.commit()
        
def add_student():
    name=input("Enter student name:")
    rollno=int(input("Enter student roll no:"))
    branch=input("Enter branch name:")
    marks=float(input("Enter student marks:"))
    try:
        with get_connection() as conn:
            cursor=conn.cursor()
            cursor.execute(
                "INSERT INTO Student(name,rollno,branch,marks) VALUES(?,?,?,?)",(name,rollno,branch,marks)
            )
            conn.commit()
    except sqlite3.IntegrityError:
        print("user with roll no is already exist")

def view_students():
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT * FROM Student"
        )
        rows=cursor.fetchall()

        if not rows:
            print("no student found")
            return
        for row in rows:
            id,name,rollno,branch,marks=row
            print(f"ID:{id} | NAME:{name} | ROLL NO:{rollno} | BRANCH :{branch} | MARKS :{marks} ")

def search_student():
    rollno=int(input("Enter student roll number to search:"))
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT * FROM Student WHERE rollno=?",(rollno,)
        )
        row=cursor.fetchone()
        if row:
            id,name,rollno,branch,marks=row
            print(f"ID:{id} | NAME:{name} | ROLL NO:{rollno} | BRANCH :{branch} | MARKS :{marks} ")
        else:
            print(f"student with {rollno} is not found")

def update_student():
    rollno=int(input("Enter student rollno to update:"))
    new_marks=float(input("Enter new marks:"))
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "UPDATE Student SET marks=? WHERE rollno=?",(new_marks,rollno)
        )
        conn.commit()
        print("update successful")

def delete_student():
    rollno=int(input("Enter student rollno to delete:"))
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "DELETE FROM Student WHERE rollno=?",(rollno,)
        )
        conn.commit()
        print("Delete student succesfully")
def view_toppers():
    n=int(input("Enter number to see toppers:"))
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT * FROM Student ORDER BY marks DESC LIMIT ?",(n,)
        )
        rows=cursor.fetchall()
        for row in rows:
            id,name,rollno,branch,marks=row
            print(f"ID:{id} | NAME:{name} | ROLL NO:{rollno} | BRANCH :{branch} | MARKS :{marks} ")


def main_menu():
    init_db()
    
    while True:
        print("--------STUDENT MANAGEMENT SYSTEM--------")
        print("1.ADD STUDENT:")
        print("2.VIEW STUDENT DETAILS:")
        print("3.SEARCH STUDENT BY ROLL CARD:")
        print("4.UPDATE STUDENT MARKS:")
        print("5.DELETE STUDENT:")
        print("6.view top n number of students:")
        print("7.exit...")
        choice=input("Enter your choice:")

        if choice=="1":
            add_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            search_student()
        elif choice=="4":
            update_student()
        elif choice=="5":
            delete_student()
        elif choice=="6":
            view_toppers()
        elif choice=="7":
            print("exit....")
            break
        else:
            print("Enter valid option")
    pass
if __name__=="__main__":
    main_menu()