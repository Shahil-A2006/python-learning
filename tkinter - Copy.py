"""basic structre"""
# from tkinter import *
# tab= Tk()
# tab.title('tinkinder')
# tab.mainloop()

"""to set max, min size"""
# from tkinter import *
# tab= Tk()
# tab.title('tiki tab')
# tab.geometry("500x500")
# tab.minsize(500,600)
# tab.maxsize(600,1000)
# tab.mainloop()

""""""
# from tkinter import *
# tab= Tk()
# tab.title('tiki tab')
# tab.geometry("500x500")
# tab.minsize(500,600)
# tab.maxsize(600,1000)

# a=Label(text='hello')   #to get content on tab
# a.pack()                #to align center and push content to tab

# b=Label()
# tab.mainloop()

""" basic form creation"""
# from tkinter import*
# form=Tk()
# form.title('Fill details')
# form.geometry('350x400')
# form.minsize(350,400)
# form.maxsize(350,400)
# a=Label()
# a.grid(row=0,column=0)
# fill=Label(text="Fill form",font=('calibiri',20))
# fill.grid(row=0,column=2)

# name=Label(text='Enter your name: ')
# name.grid(row=1,column=1)
# name1=Entry()
# name1.grid(row=1,column=2)
# age=Label(text='Enter your age: ')
# age.grid(row=2,column=1)
# age1=Entry()
# age1.grid(row=2,column=2)
# gen=Label(text='gender')
# gen.grid(row=3,column=1)
# male=Checkbutton(text='male')
# male.grid(row=3,column=2)
# female=Checkbutton(text='female')
# female.grid(row=3,column=3)
# sucs=Label()
# sucs.grid(row=6,column=2)

# def subbut():
#     sucs.config(text='submitted succesfully',fg='green')

# sub=Button(text='submit',command=subbut)
# sub.grid(row=4,column=2)

# form.mainloop()


""" dropdown menu.........."""
# from tkinter import *
# from tkinter.ttk import *

# drop=Tk()
# drop.geometry('500x500')

# c=Combobox()
# c['values']=('Select country','Australia','China','Denmark','England','France','India','Russia')
# c.grid(row=0,column=0)
# c.current(0)

# a=Label()
# a.grid(row=1,column=1)
# def clk():
#     opt=c.get()
#     a.config(text=opt)

# b=Button(text='OK',command=clk)
# b.grid(row=0,column=1)

# drop.mainloop()

"""message box(warning/info/error)"""
# from tkinter import *
# from tkinter import messagebox
# msg=Tk()
# msg.geometry('500x500')

# def cont():
#     messagebox.showinfo('info','Are you sure want to continue')
#     messagebox.showwarning('warning','Continue may cause unspecified error')
#     messagebox.showerror('error_606','Your system has been Encrypetd')

# btn=Button(text='continue',command=cont)
# btn.grid(row=0,column=0)

# msg.mainloop()


"""checkbox"""

# from tkinter import*
# tab=Tk()
# tab.title('check_box')
# tab.geometry('500x500')

# x=Label(text='select languages')
# x.grid(row=0,column=0)

# def ok():
#     selected=[]
#     for i,j in enumerate(chkbxvar):
#         if j.get()==1:
#             selected.append(languages[i])
#     print(selected)


# languages=['python','c++','html','javascript','java','ruby']
# chkbxvar=[]
# for i in languages:
#     var=IntVar()
#     chkbx=Checkbutton(text=i, variable=var)
#     chkbx.grid(sticky=W)
#     chkbxvar.append(var)

# sub=Button(text='submit',command=ok)
# sub.grid(row=8,column=0)


# tab.mainloop()


"""radio button"""
# from tkinter import *
# from tkinter.ttk import *
# root=Tk()
# root.title("radio button")
# root.geometry("500x600")

# selected=StringVar()
# selected1=StringVar()

# t=Label(text="GENDER")
# t.grid(row=0,column=0)
# radio=Radiobutton(text="MALE",value="MALE",variable=selected)
# radio.grid(row=0,column=1)
# radio=Radiobutton(text="FEMALE",value="FEMALE",variable=selected)
# radio.grid(row=0,column=2)

# l=Label(text="LANGUAGE")
# l.grid(row=1,column=0)
# radio1=Radiobutton(text="MALAYALAM",value="MALAYALAM",variable=selected1)
# radio1.grid(row=1,column=1)
# radio1=Radiobutton(text="ENGLISH",value="ENGLISH",variable=selected1)
# radio1.grid(row=1,column=2)
# def click():
#     print(selected.get())
#     print(selected1.get())

# btn=Button(text="click",command=click)
# btn.grid(row=3,column=3)
# root.mainloop()