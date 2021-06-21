from tkinter import*
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector
from subprocess import call
#from numba import cuda

t=Tk()
t.geometry("2000x2000")
count=1
name=""
def reg():
    treg=Toplevel()
    treg.geometry("2000x2000")
    imgX=ImageTk.PhotoImage(Image.open(r"C:\Users\karan prasad\OneDrive\Desktop\PROJECT\ss.jpg"))
    lpicX=Label(treg)
    lpicX.config(image=imgX)
    lpicX.image=imgX
    lpicX.place(x=0,y=0)
    def reg1():
        a1=tX.get()
        a2=tY.get()
        a3=tZ.get()
      
        mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="")
        my=mydb.cursor()
        my.execute("use kunal")
        my.execute("insert into data values("+"'"+a1+"'"+","+"'"+a2+"'"+","+"'"+a3+"'"+")")
        messagebox.showinfo("MessageBox","You are registered!!!")
        #mydb.commit()
        count=0
        
    if count==0:
        messagebox.showinfo("Message","Invalid Register")
        
    def clr():
        tX.delete(0,"end")
        tY.delete(0,"end")
        tZ.delete(0,"end")
    
    


    luserX=Label(treg,text="User Id",font="bold 15")
    luserX.place(x=200,y=200)
    lpassX=Label(treg,text="User Pin",font="bold 15")
    lpassX.place(x=200,y=250)
    tX=Entry(treg,font="bold 15")
    tX.place(x=320,y=200)
    tY=Entry(treg,font="bold 15")
    tY.place(x=320,y=250)
    bX=Button(treg,text="REGISTER",font="bold 20",command=reg1)
    bY=Button(treg,text="CLEAR",font="bold 20",command=clr)
    bZ=Button(treg,text="BACK",font="bold 20")#,command=treg.destroy).pack()
    
    bX.place(x=150,y=410)
    bY.place(x=350,y=410)
    bZ.place(x=500,y=410)
    lpassZ=Label(treg,text="Mobile No.",font="bold 15")
    lpassZ.place(x=200,y=300)
    tZ=Entry(treg,font="bold 15")
    tZ.place(x=320,y=300)



def login():           
    l1=t1.get()
    l2=t2.get()
      


    mydb=mysql.connector.connect(host="127.0.0.1",user="root",password="")
    my=mydb.cursor()
    my.execute("use kunal")
    my.execute("select * from data where user_name='" + l1 + "' and user_id='" + l2 + "'")
    res=my.fetchall()
    count=0
    for x in res:
            
        name=x[0]
        tprofile=Toplevel()
        tprofile.geometry("2000x2000")
        imgl=ImageTk.PhotoImage(Image.open(r"C:\Users\karan prasad\OneDrive\Desktop\PROJECT\ss.jpg"))
        lpicl=Label(tprofile)
        lpicl.config(image=imgl)
        lpicl.image=imgl
        lpicl.place(x=0,y=0)

        def vid():
            from mypack1 import ijk
            ijk()

        def img():
            from mypack2 import abc
            abc()

        def cam():
            from mypack3 import pqr
            pqr()
            
        b4=Button(tprofile,text="Video",font="bold 20",command=vid)
        b5=Button(tprofile,text="Image",font="bold 20", command=img)
        b6=Button(tprofile,text="Camera",font="bold 20", command=cam)
        lname=Label(tprofile,text="Welcome:"+name,font=("Italic Bold", 30),background="black",foreground="white")
        lname.place(x=650,y=20)
        b4.place(x=610,y=470)
        b5.place(x=730,y=470)
        b6.place(x=850,y=470)
            
        count=count+1
    if count==0:
        messagebox.showinfo("Message","Invalid Login")
            
        
       


    
img2=ImageTk.PhotoImage(Image.open(r"C:\Users\karan prasad\OneDrive\Desktop\PROJECT\x3.jpg"))
lpic2=Label(t,image=img2)
lpic2.place(x=10,y=0)
def a():
    global count
    img2=ImageTk.PhotoImage(Image.open(r"C:\Users\karan prasad\OneDrive\Desktop\PROJECT\x"+str(count)+".jpg"))
    lpic2.config(image=img2)
    lpic2.image=img2
    count=count+1
    t.after(3000,a)
    if count==5:
        count=1
a()


                                       
                                                                                                      
luser=Label(t,text="Username",font="bold 16")#, bg="#EEEEEE", fg="#555555")
luser.place(x=380,y=500)
lpass=Label(t,text="Password",font="bold 16")#, bg="#EEEEEE", fg="#555555")
lpass.place(x=780,y=500)
t1=Entry(t,font="bold 15")
t1.place(x=520,y=500)
t2=Entry(t,show="*",font="bold 15")
t2.place(x=910,y=500)
b1=Button(t,text="Register",font="bold 17",command=reg,relief=RAISED)
b2=Button(t,text="Login",font="bold 17",command=login,relief=SUNKEN)
b1.place(x=650,y=610)
b2.place(x=800,y=610)













