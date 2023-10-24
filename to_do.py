from tkinter import *
from datetime import datetime
import calendar

# global list is declare for storing all the task
tasks_list = [] 

def current_month():    
    now = datetime.now()    
    month = now.month   
    year = now.year 
    cal = calendar.month(year, month)   
    text_widget.insert(END, cal)    

def insert_new_task():
    task_string=Task_feild.get()
    if len(task_string)==0:
        Message.showinfo('Error', 'Field is Empty.')  


#------------main function----------------
if __name__ == "__main__":  

    #Creating a GUI window  
    gui = Tk()  
    #title of the window    
    gui.title("To-Do List by @deepak_kumar")      
    #size of the window 
    gui.geometry("500x500") 
    #to prevent from resizing the window    
    gui.resizable(0,0)  
    # setting the background color to #FAEBD7  
    gui.configure(bg = "#ebcabc")  


    #use for current month 
    text_widget = Text(gui, height=10, width=30, bg="#ebcabc",highlightthickness=0, borderwidth=0, font=("Helvetica", 14))
    text_widget.pack()  
    current_month() 
    
    #task enter feild 
    Task_feild = Entry(gui, width=40)   
    lable_for_submit = Label(gui, text="Enter The Task:-", bg="#ebcabc",font=("Helvetica", 14))
    
    #New task submit button
    New_task = Button(gui, text="Add New Task", command=insert_new_task,width=14)
    lable_for_submit.pack()
    Task_feild.pack()
    New_task.pack()

    #Delete task feild
    Delete_task = Button(gui, text="Delete A Task", command=insert_new_task,width=14)
    Delete_task.pack(pady=5)


    #Delete All task
    Delete_all_task = Button(gui, text="Delete All Task", command=insert_new_task,width=14)
    Delete_all_task.pack(pady=5)


    #exit button
    exit = Button(gui, text="Exit", command=insert_new_task,width=14)
    exit.pack(pady=5)

    #listbox for task
    Task_listbox = Listbox(gui, width=40, height=10)
    Task_listbox.pack()

    #mainloop is use to start the GUI   
    gui.mainloop()  
