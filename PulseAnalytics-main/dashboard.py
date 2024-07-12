from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label


ASSETS_PATH = Path(r"C:\Users\LENOVO\Downloads\PulseAnalytics-main\PulseAnalytics-main\Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def logout():
    dashboard.destroy()
    import login
    
def forms():
    dashboard.destroy()
    import forms

def graphs():
    dashboard.destroy()
    import graphs

def archive():
    dashboard.destroy()
    import archive

def reports():
    dashboard.destroy()
    import reports

dashboard = CTk()
dashboard.title("Dashboard")
x = (dashboard.winfo_screenwidth() - 1250) // 2
y = (dashboard.winfo_screenheight() - 768) // 2
dashboard.geometry(f"1250x750+{x}+{y}")
dashboard.configure(bg="#000000")

frame1 = CTkFrame(master=dashboard, fg_color="#EBEEF6", corner_radius=0, width=1250,height=750)
frame1.place(x=0, y=0)


left_frame = CTkFrame(master=frame1, fg_color="#7B66FF", corner_radius=30)
left_frame.place(relheight=0.95, relwidth=0.24, relx=0.02,rely=0.025)

right_frame = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20)
right_frame.place(relheight=0.76, relwidth=0.69, relx=0.285,rely=0.18)
background_image = PhotoImage(file=relative_to_assets("dashboard.png"))
background_label = Label(right_frame, image=background_image, borderwidth=0)
background_label.place(relx=0.5, rely=0.5,anchor="center")
right_frame.image = background_image

label1 = CTkLabel(master=frame1, text="Welcome back,",text_color="#000000", font=CTkFont('Microsoft YaHei UI Light',15,"bold"))
label1.place(relx=0.285, rely=0.05)
userlabel = CTkLabel(master=frame1, text="Username",text_color="#000000", font=CTkFont('Microsoft YaHei UI Light',30,"bold"))
userlabel.place(relx=0.285, rely=0.085)

title = CTkLabel(master=left_frame,text="PulseAnalytics",text_color="#FFFFFF",font=CTkFont('Kanit Regular', 25, "bold"))
title.place(relx=0.59, rely=0.1,anchor="center")

logo = PhotoImage(file=relative_to_assets("logo.png"))
logo_label = Label(left_frame, image=logo, borderwidth=0)
logo_label.place(relx=0.08,rely=0.075)

home_btn = CTkButton(
    master=left_frame,
    text=" Home",
    text_color="#FFFFFF",
    fg_color="transparent", 
    hover_color="#5FBDFF",
    corner_radius=20,
    font=CTkFont('Kanit Regular', 20),
    image=PhotoImage(file=relative_to_assets("home.png")),
    height=30,
    width=40,
)
home_btn.place(relx=0.5,rely=0.26,anchor="center")

form_btn = CTkButton(
    master=left_frame,
    text=" Forms",
    text_color="#FFFFFF",
    fg_color="transparent", 
    hover_color="#5FBDFF",
    corner_radius=20,
    font=CTkFont('Kanit Regular', 20),
    image=PhotoImage(file=relative_to_assets("forms.png")),
    height=30,
    width=40,
    command=forms
)
form_btn.place(relx=0.5,rely=0.37,anchor="center")

archive_btn = CTkButton(
    master=left_frame,
    text=" Archive",
    text_color="#FFFFFF",
    fg_color="transparent", 
    hover_color="#5FBDFF",
    corner_radius=20,
    font=CTkFont('Kanit Regular', 20),
    image=PhotoImage(file=relative_to_assets("archive.png")),
    height=30,
    width=40,
    command=archive
)
archive_btn.place(relx=0.5,rely=0.48,anchor="center")

Graphs_btn = CTkButton( 
    master=left_frame,
    text=" Graphs",
    text_color="#FFFFFF",
    fg_color="transparent", 
    hover_color="#5FBDFF",
    corner_radius=20,
    font=CTkFont('Kanit Regular', 20),
    image=PhotoImage(file=relative_to_assets("graphs.png")),
    height=30,
    width=40,
    command=graphs
)
Graphs_btn.place(relx=0.5,rely=0.59,anchor="center")

reports_btn = CTkButton(
    master=left_frame,
    text=" Reports",
    text_color="#FFFFFF",
    fg_color="transparent", 
    hover_color="#5FBDFF",
    corner_radius=20,
    font=CTkFont('Kanit Regular', 20),
    image=PhotoImage(file=relative_to_assets("compare.png")),
    height=30,
    width=40,
    command=reports
)
reports_btn.place(relx=0.5,rely=0.70,anchor="center")

logout_btn = CTkButton(
    master=left_frame,
    text=" Logout",
    text_color="#FFFFFF",
    fg_color="transparent",
    hover_color="#5FBDFF", 
    corner_radius=20,
    font=CTkFont('Kanit Regular', 20),
    image=PhotoImage(file=relative_to_assets("logout.png")),
    height=30,
    width=40,
    command=logout
)
logout_btn.place(relx=0.5,rely=0.88,anchor="center")




dashboard.resizable(False, False)
dashboard.mainloop()