from tkinter import *

def hello():
    print('hello world')
def say():
    print('what do you want to hear')
def about():
    w=Label(win,text='xxx')
    w.pack(side=TOP)
#home
win = Tk()
win.title('Rtt\'s search')
win.geometry('400x200')

#button
btn=Button(win,text='click me',command=hello)
btn.pack(side=LEFT)
btn2=Button(win,text="say sth",command=say)
btn2.pack()

#menu
menubar=Menu(win)
#filemenu
filemenu=Menu(menubar,tearoff=1)
filemenu.add_command(label='open',command=hello)
filemenu.add_command(label='about',command=about)
filemenu.add_separator()
filemenu.add_command(label='Quit',command=win.destroy)
menubar.add_cascade(label='File',menu=filemenu)

#show menu
win.config(menu=menubar)


win.mainloop()
