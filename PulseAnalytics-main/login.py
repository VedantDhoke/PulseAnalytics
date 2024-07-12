from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label
import pymysql

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LENOVO\Downloads\PulseAnalytics-main\PulseAnalytics-main\Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


login = CTk()
login.title("Login")
x = (login.winfo_screenwidth() - 1250) // 2
y = (login.winfo_screenheight() - 768) // 2
login.geometry(f"1250x750+{x}+{y}")
login.configure(bg="#FFFFFF")

def login_user():
    if user.get()=='' or passw.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='P@ssw0rd')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return
        query = 'use PulseAnalytics'
        mycursor.execute(query)
        query='select * from signup where username=%s and password=%s'
        mycursor.execute(query,(user.get(),passw.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid username or password')
        else:
            messagebox.showinfo('Welcome','Login is successful')
            login.destroy()
            import dashboard
            
        

            

  
        
def show():
    eye.config(file=relative_to_assets("open_eye.png")),
    passw.configure(show='')
    eyebtn.config(command=hide)
    
def hide():
    eye.config(file=relative_to_assets("close_eye.png")),
    passw.configure(show='*')
    eyebtn.config(command=show)
    
def clear():
    user.delete(0, END)
    passw.delete(0, END)
    
def signup_page():
    login.destroy()
    import signup


frame1 = CTkFrame(master=login, fg_color="#4c87ca", corner_radius=0, width=1250,height=768)
frame1.place(x=0, y=0)

background_image = PhotoImage(file=relative_to_assets("bgimg.png"))
background_label = Label(frame1, image=background_image)
background_label.place(x=0, y=0, width=1250)
frame1.image = background_image


frame2 = CTkFrame( master=frame1, fg_color="#FFFFFF", corner_radius=30, height=700, width=480)
frame2.place( x=750,y=27)


btn1 = CTkButton(
    master=frame2,
    text="Login",
    corner_radius=30,
    fg_color="#5FBDFF",
    hover_color="#7B66FF",
    width=150,
    height=60,
    font=CTkFont(size=20, weight="bold"),
    command=login_user,
    text_color="#000000",
)
btn1.place(relx=0.53,rely=0.76)


btn2 = CTkButton(
    master=frame2,
    text="Clear",
    text_color="#000000",
    corner_radius=30,
    fg_color="transparent",
    hover_color="#FF2D3F",
    border_width=2,
    border_color="black",
    width=150,
    height=60,
    font=CTkFont(size=20, weight="bold"),
    command=clear
)

btn2.place(relx=0.16,rely=0.76)

user = CTkEntry(
    master=frame2,
    corner_radius=100,
    width=400,
    height=70,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Login Id",
    text_color="#000000",
    font=CTkFont(family="Kanit Regular",size=20)
)
user.place(y=305,x=41
)

passw = CTkEntry(
    master=frame2,
    show='*',
    corner_radius=50,
    width=400,
    height=70,
    border_width=0,
    fg_color="#D6D6D6",
    placeholder_text="Password",
    text_color="#000000",
    font=CTkFont(family="Kanit Regular",size=20),
)
passw.place(y=410,x=41)


eye = PhotoImage(file=relative_to_assets("close_eye.png"))
eyebtn = Button(
    frame2,
    borderwidth=0,
    image=eye,
    highlightthickness=0,
    highlightbackground="#D6D6D6",
    command=show,
    cursor="hand2"
)
eyebtn.place(x=494, y=558, anchor="center")

title1=CTkLabel(
    master=frame2,
    text="Login",
    text_color="#000000",
    font=CTkFont(family="Microsoft YaHei UI Light", size=50,weight="bold")
)
title1.place(x=162,y=195)

profile_img=PhotoImage(file=relative_to_assets("profile.png"))
profile=Label(
    master=frame2,
    image=profile_img,
    borderwidth=0,
).place(x=298,y=140,anchor="center")

label=Label(frame2,text="Don't have an account yet?",fg='black',bg='white',font=('Microsoft YaHei UI Light',11)).place(x=255, y=810,anchor="center")
sign_up= Button(frame2,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#57a1f8',font=CTkFont('Microsoft YaHei UI Light',16), command=signup_page).place(x=380, y=810,anchor="center")

login.resizable(False, False)
login.mainloop()