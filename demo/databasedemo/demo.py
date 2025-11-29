import sqlite3

conn=sqlite3.connect("students.db")
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    rollno INTEGER UNIQUE,
    branch text,
    marks REAL
    )

""")
conn.commit()

def add_values(name,rollno,branch,marks):
    cursor.execute(
        "INSERT INTO Students(name,rollno,branch,marks) VALUES (?,?,?,?)",(name,rollno,branch,marks)
    )
    conn.commit()
# add_values("tarun",575,"cse",100)
add_values("ravi",580,"ece",90)

def fetch_data():
    cursor.execute("select * from Students")
    rows=cursor.fetchall()
    for row in rows:
        print(row)
# fetch_data()

def filter_data(rollno):
    cursor.execute("select * from Students where rollno=?",(rollno,))
    rows=cursor.fetchone()
    print(rows)
# filter_data(575)

def update_marks(new_marks,rollno):
    cursor.execute(
        "update Students SET marks=? where rollno=?",(new_marks,rollno)
    )
    conn.commit()
# update_marks(200,580)
# fetch_data()

def delete_row(rollno):
    cursor.execute(
        "delete from Students where rollno=?",(rollno,)
    )
    conn.commit()
# delete_row(580)
conn.close()