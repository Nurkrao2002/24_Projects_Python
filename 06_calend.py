#Importing tkinter module
from tkinter import *
#importing calendar module
import calendar

#function to show calendar of the given year
def showCalender():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calender for the year")
    gui.geometry("550x900")
    year = int(year_field.get())
    gui_content= calendar.calendar(year)
    calYear = Label(gui, text= gui_content, font= "Consolas 10 bold")
    calYear.grid(row=5, column=1,padx=20)
    gui.mainloop()

#Driver code
if __name__=='__main__':
    new = Tk()
    new.config(background='black')
    new.title("Calender")
    new.geometry("250x150")
    cal = Label(new, text="Calender",bg='indianred',font=("times", 18, "bold"))
    year = Label(new, text="Enter year", bg='yellow')
    year_field=Entry(new)
    button = Button(new, text='Show Calender',
fg='Black',bg='lime',command=showCalender)

    #putting widgets in position
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    button.grid(row=5, column=1)
    # Exit.grid(row=6, column=1)
    new.mainloop()