import sqlite3
conn= sqlite3.connect("Expenditure.db")

#Creating cursor
c=conn.cursor()

#Creating Expenditure Table
def var_push_expense(date,where_s,amt):
    c.execute("""CREATE TABLE IF NOT EXISTS expenditures(
            date TEXT,
            reason TEXT,
            amount REAL
        )""")

    records = [(date, r, a) for r, a in zip(where_s, amt)]

    c.executemany(
        """INSERT INTO expenditures (date, reason, amount) 
        VALUES(?,?,?)""", records )

    conn.commit()


    c.execute("SELECT * FROM expenditures")

    data = c.fetchall()
    print(data) 

    
#Creating Loan Table
def var_push_loans(datel,lender,cost,why):
    c.execute("""CREATE TABLE IF NOT EXISTS loans(
            date TEXT,
            lender TEXT,
            amount  TEXT,
            reason TEXT
        )""")

    c.executemany(
        """INSERT INTO loans (date, lender, amount,reason) 
        VALUES(?,?,?,?)""", [(datel,lender,cost,why)] )

    conn.commit()


    c.execute("SELECT * FROM loans")

    loas = c.fetchall()
    print(loas) 



