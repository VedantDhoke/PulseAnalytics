from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label
import pymysql

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LENOVO\Downloads\PulseAnalytics-main\PulseAnalytics-main\Assets")

def clear():
    name.delete(0,END)
    username.delete(0,END)
    phone.delete(0,END)
    password.delete(0,END)
    confirm_password.delete(0,END)


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


signup = CTk()
signup.title("Signup") 
x = (signup.winfo_screenwidth() - 1250) // 2
y = (signup.winfo_screenheight() - 768) // 2
signup.geometry(f"1250x768+{x}+{y}")
signup.configure(bg="#FFFFFF")

def connect_database():
    if name.get()=='' or username.get()=='' or phone.get()=='' or password.get()=='' or confirm_password.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif password.get() != confirm_password.get():
        messagebox.showerror('Error','Password Mismatch')
    elif len(phone.get())!=10 :
         messagebox.showerror("Error","Invalid Phone Number")

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='P@ssw0rd')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
            query='create database PulseAnalytics'
            mycursor.execute(query)
            query='use PulseAnalytics'
            mycursor.execute(query)
            query='create table signup(id int auto_increment primary key not null, name varchar(25),username varchar(50), phone varchar(50), password varchar(50) )'
            mycursor.execute(query)
        except:
            mycursor.execute('use PulseAnalytics')
        query='select * from signup where username=%s'
        mycursor.execute(query,(username.get()))    

        row=mycursor.fetchone() 
        if row != None:
              messagebox.showerror('Error','Login Id Already Exists')
        else:

            query='insert into signup(name,username,phone,password) values(%s,%s,%s,%s)'   
            mycursor.execute(query,(name.get(),username.get(),phone.get(),password.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration Is Successful')
            clear()
            signup.destroy()
            import login
              
                 
def login_page():
    signup.destroy()
    import login       
        
    

frame1 = CTkFrame(master=signup, fg_color="#4c87ca", corner_radius=0, width=1250,height=768)
frame1.place(x=0, y=0)

background_image = PhotoImage(file=relative_to_assets("bgimg2.png"))
background_label = Label(frame1, image=background_image)
background_label.place(x=0, y=0, width=1250)
frame1.image = background_image


frame2 = CTkFrame( master=frame1, fg_color="#FFFFFF", corner_radius=30, height=700, width=700)
frame2.place( relx=0.25,y=35)

title1=CTkLabel(
    master=frame2,
    text="Create an Account",
    text_color="#000000",
    font=CTkFont(family="Microsoft YaHei UI Light", size=50,weight="bold")
)
title1.place(relx=0.51,y=65, anchor="center")

name = CTkEntry(
    master=frame2,
    corner_radius=50,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Name",
    font=CTkFont(family="Kanit Regular",size=20),
    text_color="#000000"
)
name.place(y=165,relx=0.51,anchor="center")

username = CTkEntry(
    master=frame2,
    corner_radius=50,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Login Id",
    font=CTkFont(family="Kanit Regular",size=20),
    text_color="#000000"
)
username.place(y=245,relx=0.51,anchor="center")

phone = CTkEntry(
    master=frame2,
    corner_radius=100,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Phone No",
    font=CTkFont(family="Kanit Regular",size=20),
    text_color="#000000"
)
phone.place(y=325,relx=0.51,anchor="center")

password = CTkEntry(
    master=frame2,
    corner_radius=50,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Password",
    font=CTkFont(family="Kanit Regular",size=20),
    text_color="#000000"
    )

password.place(y=405,relx=0.51,anchor="center")
    
confirm_password = CTkEntry(
    master=frame2,
    corner_radius=100,
    width=400,
    height=50,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Confirm Password",
    font=CTkFont(family="Kanit Regular",size=20),
    text_color="#000000"
)
confirm_password.place(y=485,relx=0.51,anchor="center")

btn1 = CTkButton(
    master=frame2,
    text="Sign Up",
    corner_radius=30,
    fg_color="#5FBDFF",
    hover_color="#7B66FF",
    width=150,
    height=60,
    font=CTkFont(size=20, weight="bold"),
    text_color="#000000",
    command=connect_database
)
btn1.place(relx=0.5,y=585, anchor="center")

label=Label(frame2,text="Already have an account ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',11)).place(x=400, y=820,anchor="center")
log_in= Button(frame2,width=6,text='Login',border=0,bg='white',cursor='hand2',fg='#57a1f8',font=CTkFont('Microsoft YaHei UI Light',16), command=login_page).place(x=519, y=820, anchor="center")



signup.resizable(False,False)
signup.mainloop()