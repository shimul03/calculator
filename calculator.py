from tkinter import *
from tkinter.font import BOLD
from math import sqrt
#import math

def btnclick(numbers):
    global operator
    operator=operator + str(numbers)
    text_input.set(operator)
    
def btnclear():
    global operator
    operator="" 
    text_input.set(operator) 

def btnequal():
    global operator
    sum=str(eval(operator)) 
    text_input.set(sum)
    operator=""  

def btnsqureroot():
    global operator
    sum=eval(operator)
    x=sqrt(sum)
    text_input.set(x)
    
'''def btnsqureroot(text_input):
    x=math.sqrt(text_input)
    return x'''
    
      
    
       

cal=Tk()
cal.title("calculator")
operator=""
text_input=StringVar()

txtdisplay=Entry(cal, font=('arial', 20, BOLD), textvariable=text_input, bd=30, insertwidth=4, bg="powder blue", justify='right').grid(columnspan=4)

#............First Row
btn7=Button(cal, padx=16, bd=8, bg="powder blue", fg="black" , font=('arial',20,'bold'),text="7", command=lambda:btnclick(7)).grid(row=1,column=0 )

btn8=Button(cal, padx=16, bd=8, bg="powder blue", fg="black" , font=('arial',20,'bold'),text="8",command=lambda:btnclick(8)).grid(row=1,column=1 )

btn9=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="9",command=lambda:btnclick(9)).grid(row=1,column=2 )

Addbtn=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="+",command=lambda:btnclick("+")).grid(row=1,column=3 )

#...............2nd ROW
btn4=Button(cal, padx=16, bd=8, bg="powder blue", fg="black",  font=('arial',20,'bold'),text="4",command=lambda:btnclick(4)).grid(row=2,column=0 )

btn5=Button(cal, padx=16, bd=8, bg="powder blue", fg="black" , font=('arial',20,'bold'),text="5",command=lambda:btnclick(5)).grid(row=2,column=1 )

btn6=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="6",command=lambda:btnclick(6)).grid(row=2,column=2 )

Subbtn=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="-",command=lambda:btnclick("-")).grid(row=2,column=3 )


#.................3rd ROW
btn1=Button(cal, padx=16, bd=8, bg="powder blue", fg="black" , font=('arial',20,'bold'),text="1",command=lambda:btnclick(1)).grid(row=3,column=0 )

btn2=Button(cal, padx=16, bd=8, bg="powder blue", fg="black" , font=('arial',20,'bold'),text="2",command=lambda:btnclick(2)).grid(row=3,column=1 )

btn3=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="3",command=lambda:btnclick(3)).grid(row=3,column=2 )

mulbtn=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="*",command=lambda:btnclick("*")).grid(row=3,column=3 )

#.................4th Row

btn7=Button(cal, padx=16, bd=8, bg="powder blue", fg="black" , font=('arial',20,'bold'),text="0",command=lambda:btnclick(0)).grid(row=4,column=0 )

clearbtn=Button(cal, padx=16, bd=8, bg="powder blue", fg="black" , font=('arial',20,'bold'),text="c",command=btnclear).grid(row=4,column=1 )

equalbtn=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="=",command=btnequal).grid(row=4,column=2 )

divbtn=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="/",command=lambda:btnclick("/")).grid(row=4,column=3 )

squarbtn=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="^",command=lambda:btnclick("**")).grid(row=5,column=2 )

modbtn=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="%",command=lambda:btnclick("%")).grid(row=5,column=3 )

squarrotbtn=Button(cal, padx=16, bd=8,bg="powder blue", fg="black" , font=('arial',20,'bold'),text="sqrt",command=btnsqureroot).grid(row=5,column=1 )
cal.mainloop()


