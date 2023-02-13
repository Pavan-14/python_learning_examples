''' The goal of this project is to create a personal budgeting app that allows users to track their income and expenses, set budget goals, and view their spending habits.

Here are the steps you can take to create this project:

    Use the sqlite3 library to create a database to store the user's budget data.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons, text boxes and tables.

    Use the pandas library to manipulate the data and generate charts and tables to visualize the user's budget data.

    Use the datetime library to store and display the date and time of the transactions. '''


# importing tkinter module
from tkinter import *
from tkinter import messagebox
from tkcalendar import *
import database
import pandas as pd
import os


# creating a dispaly for my budget application
display = Tk()


# title for display
display.title("Budget Application")
# adding configuration to dispaly screen
display.config(bg="skyblue")
# add icon to application page
display.iconbitmap(r"E:\Pavan Learnings\Braineest\week_01\personal_budget_app\budgeticon.ico")
# dispaly size
display.geometry("1000x500")



# creating a label with application name
application_name = Label(display,text="Personal Budget Tracking",fg="red",font="20",width="1000",
                         height="3",cursor="dot",relief=RAISED)
application_name.pack()

# creating calendar instance
cale = Calendar(display, selectmode="day", date_pattern="dd-mm-y")

'''function created to get the date'''
def grab_date():
    date = date_label.config(text=cale.get_date())
    return cale.get_date()

# the function created to create excel file and also import the data from database tables to excel file
def generate_report():
    # database file path variable
    database_filepath = database.database_path

    # calling database connection function
    database_conncetion = database.create_connection(database_filepath)
    # print(database_conncetion)

    # checking the database conection result
    if database_conncetion is not None:
        # the conection is ok, then

        # new excel file for store the data
        excel_filename = "budget_tracking.xlsx"
        # the full excel file path
        excel_filepath = os.path.join(os.getcwd(),excel_filename)
        # create a writer to write the data
        with pd.ExcelWriter(excel_filepath,engine="openpyxl",date_format="DD-MM-YYYY") as writer:

            # use pandas dataframe to get all tables inside the database
            df = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table'",database_conncetion)
            # print(df["name"]) # prints the tables inside the database_conncetion database

            for table_name in df["name"]:
                # sql query statement variable
                sql_query = "SELECT * FROM "+table_name
                # print(sql_query)
                # creating the dataframe for each table data
                df_tablesdata = pd.read_sql(sql_query,database_conncetion)

                # load the data to excel file
                df_tablesdata.to_excel(writer,sheet_name=table_name,index=False)

                messagebox.showinfo("Report generator",excel_filename+" updated succesfully.")
            database_conncetion.close()



'''creating function to add budget details'''
def budget_values_insert():
    # get the value from the type varibale used in radio buttons
    choice_type = type.get()
    # get the value from the entry (form)
    item_name = item.get()
    # get the value from the entry (form)
    amount_value = amount.get()
    # get the date
    date = grab_date()


    # creating tables inside database
    database.main()
    # inserting values into table
    database.insert_values(choice_type,item_name,amount_value,date)
    messagebox.showinfo("data added",item_name+" "+str(amount_value)+"euros"+"added to"+" "+choice_type+"table"+str(date))
    generate_report()
    '''
    # if user choices income add amount to income
    if choice_type.casefold() == "income".casefold():
        messagebox.showinfo("Income information","income amount is added to budget.")

    elif choice_type.casefold() == "expense".casefold():
        messagebox.showinfo("expense information","expense amount is deleted from the budget amount.")
    else:
        messagebox.askretrycancel('retry', 'choose the type')
    '''

    # clears the enter values after hitting submit button
    item_entry.delete(0,END)
    amount_entry.delete(0,END)
    income_button.deselect()
    expense_button.deselect()



# created labels variables
item_txt = Label(display,text="Enter item *")
amount_txt = Label(display,text="Enter amount *")
type_txt = Label(display,text="Choice type *")

# place the labels on display screen
item_txt.place(bordermode=OUTSIDE,x=10,y=80)
amount_txt.place(bordermode=OUTSIDE,x=10,y=130)
type_txt.place(bordermode=OUTSIDE,x=10,y=180)

'''create varibles to enter the values'''
# create itemvariable and entry widget
item= StringVar()
item_entry = Entry(display,textvariable=item,width="60")
item_entry.place(x=100,y=80,bordermode=OUTSIDE)

# create amount variable and entry widget
amount = IntVar()
amount_entry = Entry(display,textvariable=amount,width="20")
amount_entry.place(x=100,y=130,bordermode=OUTSIDE)


# create type variable and radio buttons
type = StringVar()
income_button = Radiobutton(display,text="Income", variable=type, value="income",activebackground="green")
expense_button = Radiobutton(display,text="Expense", variable=type, value="expense",activebackground="red")
income_button.place(x=10,y=210)
expense_button.place(x=100,y=210)

# add a button to Today date
date_button = Button(text="Today date", command=grab_date)
date_button.place(x=10,y=350)

# date label (optional)
date_label = Label(display,text="",width=40)
date_label.place(x=10,y=270)


# add a button to submit
submit_button = Button(display,text="Submit",fg="green",bg="grey",font="12",width="10",height="1",relief=RAISED,command=budget_values_insert)
submit_button.place(x=10,y=450)

display.mainloop()
