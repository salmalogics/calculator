
from tkinter import *
from tkinter.ttk import*

from setuptools import Command


window=Tk()
window.title("Calculater")
window.geometry("450x200")
window.maxsize(600,400)
window.minsize(300,200)

y=Entry(window)
# y.grid(row=1)
y.grid(columnspan=12,row=2)
y.focus()

def a():
    
   
    y.insert(END,"1")
    print("1")
b=Button(window,text="1",command=a,)
b.grid(column=1,row=5)

def b():
    
    y.insert(END,"2")
    print("2")
b2=Button(window,text="2",command=b)
b2.grid(column=2,row=5)

def c():
   
    y.insert(END,"3")
    print("3")
b3=Button(window,text="3",command=c)
b3.grid(column=3,row=5)





def d():
   
    y.insert(END,"4")
    print("4")
b4=Button(window,text="4",command=d)
b4.grid(column=1,row=4)

def e():
    y.insert(END,"5")
    print("5")
b5=Button(window,text="5",command=e)
b5.grid(column=2,row=4)

def f():

    y.insert(END,"6")
    print("6")
b6=Button(window,text="6",command=f)
b6.grid(column=3,row=4)





def g():
    
    y.insert(END,"7")
    print("7")
b7=Button(window,text="7",command=g)
b7.grid(column=1,row=3)


def i():
  
    y.insert(END,"8")
    print("8")
b9=Button(window,text="8",command=i)
b9.grid(column=2,row=3)

def j():
    
    y.insert(END,"9")
    print("9")
b10=Button(window,text="9",command=j)
b10.grid(column=3,row=3)







def k():
    u=y.get()

    if u=='0':
        # print(1)
        # y.delete(1,END)
        y.configure(text="0")
    
    else:
        y.insert(END,"0")
        print("0")
b11=Button(window,text="0",command=k)
b11.grid(column=2,row=6)

# -------------------------additional fns-----------.

def zerofind():
    u=y.get()
    if u=="01":
        y.delete('0')
        y.insert("1")
      
    elif u=='02':
        y.delete('0')
        y.insert("2")
    elif u=='03':
        y.delete('0')
        y.insert("3")
    elif u=='04':
        y.delete('0')
        y.insert("4")
        
    elif u=='05':
        y.delete('0')
        y.insert("5")
    elif u=='06':
        y.delete('0')
        y.insert("6")
    elif u=='07':
        y.delete('0')
        y.insert("7")
    elif u=='08':
        y.delete('0')
        y.insert("8")
    elif u=='09':
        y.delete('0')
        y.insert("9")



def op(c):
    
    c=c
    if c==0:
        exit
    else:
        if c==1:
            # u=len(y.get())
        
            y.delete(2)
        
            


# -------------------------------end------------------

# ============arithmatic===========

def m():

    op(c)
    zerofind()
    y.insert(END,"+")
    print("+")
b13=Button(window,text="+",command=m)
b13.grid(column=4,row=4)
c=1
def n():
    
    op(c)
    zerofind()
    y.insert(END,"-")
    print("-")
b14=Button(window,text="-",command=n)
b14.grid(column=4,row=3)
c=1
def o():
    
    op(c)
    zerofind()
    y.insert(END,"*")
    print("x")
b15=Button(window,text="x",command=o)
b15.grid(column=4,row=2)
c=1


def p():

    op(c)
    zerofind()
    y.insert(END,"/")
    print("/")
b16=Button(window,text="/",command=p)
b16.grid(column=4,row=5)
c=1


# ---------------end arithmatic....................
def q():
    y.delete(0,END)
    print("clear")
b17=Button(window,text="clear",command=q)
b17.grid(column=1,row=6)





def l():
    m=y.get()
    zerofind()
    n=eval(m)
    q()
    y.insert(END,n)
    print("=")
b12=Button(window,text="=",command=l)

b12.grid(column=4,row=6)









def r():
    n=len(y.get())
    y.delete(n-1,END)
    print("<")
b17=Button(window,text="<",command=r)
b17.grid(column=3,row=6)

window.mainloop()