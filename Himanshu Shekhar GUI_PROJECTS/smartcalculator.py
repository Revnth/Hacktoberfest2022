from tkinter import *
def add(a,b):
    return a+b
def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def mod(a,b):
    return a%b

def lcm(a,b):
    l=a if a>b else b
    while l<=a*b:
        if l%a==0 and l%b==0:
            return l
        l+=1

def hcf(a,b):
    l=a if a<b else b
    while l>=1:
        if a%l==0 and b%l==0:
            return l
        l-=1


operation={'ADD':add,'ADDITION':add,'PLUS':add,'SUM':add,'SUB':sub,'SUBTRACT':sub,'MINUS':sub,'DIFFERENCE':sub,'PRODUCT':mul, 'MULTIPLY':mul, 'MUL':mul, 'DIVIDE':div, 'DIVISION':div, 'DIV':div, 'MOD':mod ,'REMAINDER':mod}

def extract(text):
    o=[]
    for t in text.split(' '):
        try:
            o.append(float(t))
        except ValueError:
            pass

    return o
def calculate():
    text=textin.get()
    for word in text.split(' '):
        if word.upper() in operation.keys():
            try:
                l=extract(text)
                r=operation[word.upper()](l[0],l[1])
                list.delete(0,END)
                list.insert(END,r)
            except:
                list.delete(0,END)
                list.insert(END,'something wrong occured while calculating please enter again correctly')
            finally:
                break

        elif word.upper() not in operation.keys():
            list.delete(0,END)
            list.insert(END,'something wrong occured while calculating please enter again correctly')



win=Tk()
win.geometry('600x500')
win.title('SMART CALCULATOR')
win.configure(bg='lightgreen')

l1=Label(win,text='Welcome to the world of smart calculator',width=40,padx=4)
l1.place(x=150,y=10)
l1=Label(win,text='You are using HS programmed calculator',width=35,padx=4)
l1.place(x=180,y=40)
l1=Label(win,text='Please enter your problem below with proper space',width=40,padx=4)
l1.place(x=140,y=130)

textin= StringVar()
e1=Entry(win,textvariable=textin,width=50)
e1.place(x=140,y=170)

b1=Button(win,text="CALCULATE",command=calculate)
b1.place(x=210,y=200)

list=Listbox(win, width=80, height=4)
list.place(x=100,y=230)

b5=Button(win,text='CLOSE',width=12,pady=5,padx=4,command=win.destroy)
b5.place(x=250,y=340)
win.mainloop()
