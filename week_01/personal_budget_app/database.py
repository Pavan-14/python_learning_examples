import sqlite3
from sqlite3 import Error


database_path = r"E:\Pavan Learnings\Braineest\week_01\personal_budget_app\budget.db"

def create_connection(db_file):
    """ create a database connection to the SQLite database specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return: None
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        print(f"table created in  budget database")
        # database connection closing
        connection_close(database_path)
    except Error as e:
        print(e)

def insert_values(type:str,item_name,amount,created_date):
    """ onnect to database and inserting values """ 
    conn = create_connection(database_path)
    if conn is not None:
        """ Insert values into tables """
        # if type.casedfold() == "income".casefold():
        if type == "income":
            insert_income_values = "INSERT INTO income_table VALUES(NULL,?,?,?)"
            income_cursor = conn.cursor()
            income_cursor.execute(insert_income_values,(item_name,amount,created_date))
            conn.commit()
            print("the income record updated")
            connection_close(database_path)
        # elif type.casedfold() == "expense".casefold():
        elif type == "expense":
            expense_insert_values = """INSERT INTO expense_table VALUES(NULL,?,?,?);"""
            expense_cursor = conn.cursor()
            expense_cursor.execute(expense_insert_values,(item_name,amount,created_date))
            conn.commit()
            print("the expense record updated")
            connection_close(database_path)
        else:
            print("select the type of amount")
    else:
       print("Error! cannot create the database connection.") 


def connection_close(database_path):
    # close the connection
    create_connection(database_path).close()




def main():

    income_table = """CREATE TABLE IF NOT EXISTS income_table (id INTEGER PRIMARY KEY,item_name TEXT NOT NULL,
                                                                amount NUMERIC NOT NULL,entered_date DATE);"""

    expense_table = """CREATE TABLE IF NOT EXISTS expense_table (id INTEGER PRIMARY KEY,item_name TEXT NOT NULL,
                                                                amount NUMERIC NOT NULL,entered_date DATE);"""

    # create a database connection
    conn = create_connection(database_path)

    # create tables
    if conn is not None:
        # create income table
        create_table(conn, income_table)

        # create expense table
        create_table(conn, expense_table)

    else:
        print("Error! cannot create the database connection.")
    
"""
if __name__ == '__main__':
    main()
"""