from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label



ASSETS_PATH = Path(r"C:\Users\LENOVO\Downloads\PulseAnalytics-main\PulseAnalytics-main\Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def logout():
    archive.destroy()
    import login
    
def home():
    archive.destroy()
    import dashboard
    
def forms():
    archive.destroy()
    import forms
    
def graphs():
    archive.destroy()
    import graphs

def reports():
    archive.destroy()
    import reports
    
def bbc_archive():
    archive.destroy()
    import cbc_archive
    
def cbc_archive():
    archive.destroy()
    import cbc_archive

archive = CTk()
archive.title("PulseAnalytics")
x = (archive.winfo_screenwidth() - 1250) // 2
y = (archive.winfo_screenheight() - 768) // 2
archive.geometry(f"1250x750+{x}+{y}")
archive.configure(bg="#000000")

frame1 = CTkFrame(master=archive, fg_color="#EBEEF6", corner_radius=0, width=1250,height=750)
frame1.place(x=0, y=0)

select_label = CTkLabel(master=frame1, text="Select a form :", font=CTkFont('Microsoft YaHei UI Light',25,"bold"),text_color="#000000")
select_label.place(relx=0.285, rely=0.07)


left_frame = CTkFrame(master=frame1, fg_color="#7B66FF", corner_radius=30)
left_frame.place(relheight=0.95, relwidth=0.24, relx=0.02,rely=0.025)

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
    command=home
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
    width=40
    
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

form1 = CTkButton(master=frame1,text="Basic Blood Chemistry Test",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100, command=bbc_archive)
form1.place(relheight=0.1, relwidth=0.3, relx=0.3,rely=0.19)

form2 = CTkButton(master=frame1,text="Basic Metabolic Panel",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100)
form2.place(relheight=0.1, relwidth=0.3, relx=0.3,rely=0.34)

form3 = CTkButton(master=frame1,text="Lipid Panel(Cholesterol)",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100)
form3.place(relheight=0.1, relwidth=0.3, relx=0.3,rely=0.48)

form4 = CTkButton(master=frame1,text="Comprehensive Metabolic Panel",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100)
form4.place(relheight=0.1, relwidth=0.3, relx=0.3,rely=0.62)


form5 = CTkButton(master=frame1, text="Complete Blood Count",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100, command=cbc_archive)
form5.place(relheight=0.1, relwidth=0.3, relx=0.3,rely=0.76)

form6 = CTkButton(master=frame1, text="Heamoglobin A1c",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100)
form6.place(relheight=0.1, relwidth=0.3, relx=0.65,rely=0.19)

form7 = CTkButton(master=frame1, text="Blood Glucose(Self monitoring)",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100)
form7.place(relheight=0.1, relwidth=0.3, relx=0.65,rely=0.34)

form8 = CTkButton(master=frame1, text="Uric Acid",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100)
form8.place(relheight=0.1, relwidth=0.3, relx=0.65,rely=0.48)

form9 = CTkButton(master=frame1, text="Thyroid Stimulating Hormone",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100)
form9.place(relheight=0.1, relwidth=0.3, relx=0.65,rely=0.62)

form10 = CTkButton(master=frame1, text="Liver Function Test",font=CTkFont('Kanit Regular', 20, "bold"),fg_color="#FFFFFF",text_color="#000000",hover_color="#5FBDFF", corner_radius=100)
form10.place(relheight=0.1, relwidth=0.3, relx=0.65,rely=0.76)






archive.resizable(False, False)
archive.mainloop()