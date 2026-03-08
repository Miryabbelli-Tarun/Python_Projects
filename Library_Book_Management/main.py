import sqlite3
db_name='library_db'
def get_connection():
    return sqlite3.connect(db_name)
def create_book_table():
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS books(
                book_id INTEGER  PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                author TEXT,
                avialable INTEGER DEFAULT 1           
                       
            )
        """)
        conn.commit()
def create_table_issue_book():
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS issued_books(
                issue_id INTEGER PRIMARY KEY AUTOINCREMENT,
                book_id INTEGER,
                student_name TEXT,
                issue_date DATE DEFAULT (date('now')),
                return_date DATE DEFAULT (date('now', '+15 days')),
                status text default 'not return'  
            )
        """)
        conn.commit()

def add_book():
    title=input('Enter book name:')
    author=input('Enter book author name:')

    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "INSERT INTO books(title,author) VALUES (?,?)",
            (title,author)
        )
        conn.commit()
        print('book added succesfully')
def show_books():
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "select * from books"
        )
        rows=cursor.fetchall()
        print('----------------all books--------------')
        for row in rows:
            avialable='avialable' if row[3]==1 else 'issued'
            print(f'{row[0]}|{row[1]}|{row[2]}|{avialable}')
def issue_book():
    book_id=int(input('Enter book id:'))
    student_name=input('Enter student name:')

    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "SELECT avialable FROM books WHERE book_id=?",(book_id,)
        )
        book=cursor.fetchone()
        if book and book[0]==1:
            cursor.execute(
                "INSERT INTO issued_books(book_id,student_name) VALUES(?,?)",(book_id,student_name)
            )
            cursor.execute(
                "UPDATE books SET avialable=0 WHERE book_id=?",(book_id,)
            )

            conn.commit()
            print('book issued succesfully')
        else:
            print('book is not avialble')

def search_book_avialablity():
    book_id=int(input('Enter book id:'))
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "select * from books where book_id=?",(book_id,)
        )
        book=cursor.fetchone()
        if book and book[3]==1:
            print(f'{book[1]} is avialabel')
        else:
            print('book is not avialable')
def return_book():
    issue_id=int(input('Enter book issue id:'))
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "UPDATE issued_books set status='returned' WHERE issue_id=?",(issue_id,)
        )
        conn.commit()
        print('book returned succesfull')

def delete_book():
    book_id=int(input('Enter book id:'))
    with get_connection() as conn:
        cursor=conn.cursor()
        cursor.execute(
            "select * from books where book_id=?",(book_id,)
        )
        book=cursor.fetchone()
        if book:
            cursor.execute(
                "DELETE FROM books WHERE book_id=?",(book_id,)
            )
            conn.commit()
            print('book delete succesfully')
        else:
            print('no book found')
def main():
    create_book_table()
    create_table_issue_book()
    while True:
        print('=============library management system==================')
        print('1.add new book')
        print('2.view all books')
        print('3.issue book')
        print('4.search book is avialable or not')
        print('5.return book')
        print('6.Delete book')
        print('10.exit')

        choice=input('Enter your choice:')

        if choice=='1':
            add_book()
        elif choice=='2':
            show_books()
        elif choice=='3':
            issue_book()
        elif choice=='4':
            search_book_avialablity()
        elif choice=='5':
            return_book()
        elif choice=='6':
            delete_book()
        elif choice=='10':
            break
        else:
            print('Please ..Enter a valid choice')

if __name__=='__main__':
    main()
