#! .\pythonw.exe
#===========================================TIME MODULE==================================
from tkinter import *
import time
#===========================================DISPLAY======================================
root = Tk()
root.title("Clock")
width = 600
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2)- (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.config(bg="black")
#===========================================FRAMES========================================
Top = Frame(root, width=600, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=600)
Mid.pack(side=TOP, expand=1)
#===========================================LABEL WIDGET==================================
lbl_title = Label(Top, text="Clock", width=600, font=("arial", 20))
lbl_title.pack(fill=X)
#===========================================MAIN WIDGET===================================
clock = Label(Mid, font=('times', 50 , 'bold'), fg="red", bg="black")
clock.pack()
#===========================================SETUP CLOCK===================================
def tick():
    setTime = time.strftime('%I:%M:%S %p')
    clock.config(text=setTime )
    clock.after(200, tick)
#===========================================INITIALIZATION================================
 
if __name__ == '__main__':
    tick()
    root.mainloop()
#===========================================END===========================================
