from tkinter.font import BOLD
from mysql_connector import *
from tkinter import *
from tkinter import messagebox, filedialog, simpledialog
from tkcalendar import Calendar, DateEntry

root = Tk()
root.title("Employee")
# root.geometry("750x500")

title = Label(root, text="Employee", font='Helvetica 18 bold').grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def insertEmployee():
    name = nameInsert.get()
    contact = contactInsert.get()
    location = locationInsert.get()
    joined_date = date.get_date()
    profession = professionInsert.get()

    if name == "":
        messagebox.showerror('Name field empty', 'Please, enter your name', parent=root)
        nameInsert.focus_force()
    elif contact == "":
        messagebox.showerror('Contact field empty', 'Please, enter contact of ' + name, parent=root)
        contactInsert.focus_force()
    elif location == "":
        messagebox.showerror('Location field empty', 'Please, enter address of ' + name, parent=root)
        locationInsert.focus_force()
    elif joined_date == "":
        messagebox.showerror('Joined Date', 'Select joined date of ' + name, parent=root)
    elif profession == "":
        messagebox.showerror('Name field empty', 'Please, enter profession of ' + name, parent=root)
        professionInsert.focus_force()
    else:
        mycursor = mydb.cursor()

        sqlInsert = "INSERT INTO `employee`(`name`, `contact`, `location`, `joined_date`, `profession`) " \
                    "VALUES (%s,%s,%s,%s,%s)"
        # employee = [{'Micheal','+17405203031','New York','12/27/2020','Office Management'},
        #             {'John','+17405203031','New York','12/27/2020','Office Management'}]
        # mycursor.executemany(sqlInsert,employee)
        employee = [name, contact, location, joined_date, profession]
        mycursor.execute(sqlInsert, employee)
        mydb.commit()
        if sqlInsert:
            messagebox.showinfo('Data Insert', 'Data successfully inserted', parent=root)
        else:
            messagebox.showerror('Data Insert', 'Data insert unsuccessful', parent=root)


nameLabel = Label(root, text="Name : ").grid(row=1, column=0, padx=10, pady=10)
nameInsert = Entry(root)
nameInsert.grid(row=1, column=1, padx=10, pady=10)

contactLabel = Label(root, text="Contact : ").grid(row=2, column=0, padx=10, pady=10)
contactInsert = Entry(root)
contactInsert.grid(row=2, column=1, padx=10, pady=10)

locationLabel = Label(root, text="Location : ").grid(row=3, column=0, padx=10, pady=10)
locationInsert = Entry(root)
locationInsert.grid(row=3, column=1, padx=10, pady=10)

dateLabel = Label(root, text="Joined date : ").grid(row=4, column=0, padx=10, pady=10)
date = DateEntry(root, bg="darkblue", fg="white", year=2021)
date.grid(row=4, column=1, padx=10, pady=10)

professionLabel = Label(root, text="Profession : ").grid(row=5, column=0, padx=10, pady=10)
professionInsert = Entry(root)
professionInsert.grid(row=5, column=1, padx=10, pady=10)

buttonInsert = Button(root, text="Insert Employee", command=insertEmployee)
buttonInsert.grid(row=6, column=0, padx=10, pady=10)


def updateEmployee():
    name = nameInsert.get()
    contact = contactInsert.get()
    location = locationInsert.get()
    joined_date = date.get_date()
    profession = professionInsert.get()

    checkUpdate = messagebox.askyesno('Update employee information', 'Do you want to update employee information',
                                      parent=root)
    if checkUpdate:
        userId = simpledialog.askstring('User id', 'Enter employee\'s id', parent=root)
        mycursor = mydb.cursor()

        updateEmployeeSql = "UPDATE `employee` SET `name`=%s,`contact`=%s,`location`=%s,`joined_date`=%s,`profession`=%s WHERE `id`=%s"
        value = (name, contact, location, joined_date, profession, userId)

        updateEmployee = mycursor.execute(updateEmployeeSql, value)

        mydb.commit()

        if updateEmployeeSql:
            messagebox.showinfo('Update Status', 'You have successfully updated ' + name + '\'s data')
        else:
            messagebox.showinfo('Update Status', 'You have unsuccessfully update ' + name + '\'s data')

    else:
        print('You declined update status')


buttonUpdate = Button(root, text="Update Employee", command=updateEmployee)
buttonUpdate.grid(row=6, column=1, padx=10, pady=10)


def showEmployees():
    # root.geometry("820x"+str(root.winfo_height()))
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM `employee`")

    myresult = mycursor.fetchall()
    count = mycursor.rowcount

    employees = []
    for row in myresult:
        # for i in row:
        employees.append(row)

    name = Label(root, text="Name").grid(row=0, column=2, padx=10, pady=10)
    contact = Label(root, text="Contact").grid(row=0, column=3, padx=10, pady=10)
    location = Label(root, text="Location").grid(row=0, column=4, padx=10, pady=10)
    joinedDate = Label(root, text="Joined Date").grid(row=0, column=5, padx=10, pady=10)
    profession = Label(root, text="Profession").grid(row=0, column=6, padx=10, pady=10)
    for i in range(count):
        employeesName = Label(root, text=employees[i][1]).grid(row=i + 1, column=2, padx=10, pady=10)
        employeesContact = Label(root, text=employees[i][2]).grid(row=i + 1, column=3, padx=10, pady=10)
        employeesLocation = Label(root, text=employees[i][3]).grid(row=i + 1, column=4, padx=10, pady=10)
        employeesJoinedDate = Label(root, text=employees[i][4]).grid(row=i + 1, column=5, padx=10, pady=10)
        employeesProfession = Label(root, text=employees[i][5]).grid(row=i + 1, column=6, padx=10, pady=10)


buttonShow = Button(root, text="Show employees", command=showEmployees)
buttonShow.grid(row=7, column=0, padx=10, pady=10)


def deleteEmployee():
    checkUpdate = messagebox.askyesno('Delete employee', 'Do you want to delete employee information?',
                                      parent=root)
    if checkUpdate:
        userId = simpledialog.askstring('User id', 'Enter employee\'s id', parent=root)
        mycursor = mydb.cursor()

        deleteEmployeeSql = mycursor.execute("DELETE FROM `employee` WHERE `id`="+userId+"")
        # value = (userId)

        # updateEmployee = mycursor.execute(deleteEmployeeSql, value)

        mydb.commit()

        if deleteEmployeeSql:
            messagebox.showinfo('Update Status', 'You have successfully delete ' )
        else:
            messagebox.showinfo('Update Status', 'You have unsuccessfully update ')

    else:
        print('You declined')


buttonDelete = Button(root, text="Delete employee", command=deleteEmployee)
buttonDelete.grid(row=7, column=1, padx=10, pady=10)

root.mainloop()
