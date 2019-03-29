from tkinter import *

gui = Tk()
gui.title('GV Project 2')

#Frames
top = Frame(gui, highlightbackground="blue", highlightcolor="blue", highlightthickness=1, width=100, height=100, bd= 0)
top.pack(side = TOP, fill = X, expand = True)
middle = Frame(gui, highlightbackground="blue", highlightcolor="blue", highlightthickness=1, width=100, height=100, bd= 0)
middle.pack(fill = X)
bottom = Frame(gui, highlightbackground="blue", highlightcolor="blue", highlightthickness=1, width=100, height=100, bd= 0)
bottom.pack(side = BOTTOM, fill = X)
#
#
#       TOP
#
#
#Top Labels
Label(top, text = "Connection", fg = "blue").grid(row = 0)
Label(top, text = "Server Hostname:").grid(row = 1)
Label(top, text = "Port:").grid(row = 1, column = 2)
Label(top, text = "Username:").grid(row = 2)
Label(top, text = "Hostname:").grid(row = 2, column = 2)
Label(top, text = "Speed:").grid(row = 2, column = 4)

#Top Entries
shostname = Entry(top)
username  = Entry(top)
port      = Entry(top)
hostname  = Entry(top)

shostname.grid(row = 1, column = 1)
username.grid(row = 2, column = 1)
port.grid(row = 1, column = 3)
hostname.grid(row = 2, column = 3)

#TopButton
button = Button(top, text='Connect', width=25, command=gui.destroy)
button.grid(row = 1, column = 4)

#
#
#       MIDDLE
#
#
#Middle Labels
Label(middle, text = "Search", fg = "blue").grid(row = 0, column = 0)
Label(middle, text = "Keyword:").grid(row = 1, column = 0)

#Middle Entries
keyword = Entry(middle)
keyword.grid(row = 1, column = 1)

#MiddleButton
button = Button(middle, text='Search', width=25, command=gui.destroy)
button.grid(row = 1, column = 2)

#
#
#       BOTTOM
#
#
#Bottom Labels
Label(bottom, text = "FTP", fg = "blue").grid(row = 0, column = 0)
Label(bottom, text = "Enter Command:").grid(row = 1, column = 0)

#Bottom Entries
command = Entry(bottom)
prompt = Entry(bottom)

command.grid(row = 1, column = 2)
prompt.grid(row = 2, column = 0)

#BottomButton
button = Button(bottom, text='Go', width=25, command=gui.destroy)
button.grid(row = 1, column = 2)

gui.mainloop()