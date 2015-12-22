from tkinter import *
from tkinter import ttk

def about():
    w=Label(win,text='xxx')
    w.pack(side=TOP)
def label_change():
    label["text"]=e.get()
def conact_us():
    label["text"]="has been changed"
def choose():
    label["text"]=manul_lis.get()
    
#home
win = Tk()
win.title('Rtt\'s search')
win.geometry('600x400')

#label
label=Label(win)
label.pack(side="top",fill="x",expand=1)
#label_end
vi=StringVar()
vi.set(" @NJU 2015-12-22          made by Rtt")
label2=Label(win,textvariable=vi)
label2.pack(side="bottom",fill="both",expand=0)


#listbox-titleonly_abstract
lis=StringVar()
lis.set("choose your type")
manul_lis=ttk.Combobox(win,textvariable=lis,value=["title only","title&abstract"])
manul_lis.pack(side="left")


#entry
v=StringVar()
v.set("please input here")
e=Entry(win,textvariable=v)
e.pack(side="left",fill="x",expand=1)
#e.delete(0, END)
#e.insert(0, "a default value")


#button
btn=Button(win,text='开始',command=label_change)
btn.pack(side="left",fill="x",expand=1)
btn2=Button(win,text="取消",command=win.destroy)
btn2.pack(side="left",fill="x",expand=1)

#menu
menubar=Menu(win,tearoff=0)
#filemenu
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label='open',command=about)
filemenu.add_separator()
filemenu.add_command(label='Quit',command=win.destroy)
menubar.add_cascade(label='File',menu=filemenu)
#helpmenu
helpmenu=Menu(menubar,tearoff=0)
helpmenu.add_command(label='about Rtt-search',command=about)
helpmenu.add_command(label='conact us',command=conact_us)
menubar.add_cascade(label='Help',menu=helpmenu)

#show menu
win.config(menu=menubar)


win.mainloop()
#win.update_idletasks()
