from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LENOVO\Downloads\PulseAnalytics-main\PulseAnalytics-main\Assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
    
def clear():
    date_entry.delete(0, END)
    t3_entry.delete(0, END)
    t4_entry.delete(0, END)
    tsh_entry.delete(0, END)
def submit():
    ua_forms.destroy()

ua_forms = CTk()
ua_forms.title("PulseAnalytics")
x = (ua_forms.winfo_screenwidth() - 650) // 2
y = (ua_forms.winfo_screenheight() - 550) // 2
ua_forms.geometry(f"650x550+{x}+{y}")
ua_forms.configure(bg="#000000")

frame1 = CTkFrame(master=ua_forms, fg_color="#96EFFF", corner_radius=0, width=650,height=550)
frame1.place(x=0, y=0)

title_label = CTkLabel(master=frame1, text="Thyroid Stimulating Test", font=CTkFont('Microsoft YaHei UI Light',35,"bold",underline="true"),text_color="#000000")
title_label.place(relx=0.5, rely=0.12,anchor="center")

date_label = CTkLabel(master=frame1, text="Date:", font=CTkFont('Kanit Regular',20),text_color="#000000")
date_label.place(relx=0.1,rely=0.3)
date_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="DD/MM/YYYY",text_color="#000000")
date_entry.place(relheight=0.07,relwidth=0.5,relx=0.4,rely=0.3)

t3_label = CTkLabel(master=frame1, text="T3:", font=CTkFont('Kanit Regular',20),text_color="#000000")
t3_label.place(relx=0.1,rely=0.41)
t3_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
t3_entry.place(relheight=0.07,relwidth=0.5,relx=0.4,rely=0.41)

t4_label = CTkLabel(master=frame1, text="T4:", font=CTkFont('Kanit Regular',20),text_color="#000000")
t4_label.place(relx=0.1,rely=0.52)
t4_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
t4_entry.place(relheight=0.07,relwidth=0.5,relx=0.4,rely=0.52)

tsh_label = CTkLabel(master=frame1, text="TSH:", font=CTkFont('Kanit Regular',20),text_color="#000000")
tsh_label.place(relx=0.1,rely=0.63)
tsh_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
tsh_entry.place(relheight=0.07,relwidth=0.5,relx=0.4,rely=0.63)

submit_btn = CTkButton(master=frame1,text="Submit",corner_radius=30,fg_color="#5FBDFF",hover_color="#7B66FF",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=submit)
submit_btn.place(relheight=0.08,relwidth=0.19,relx=0.65,rely=0.87,anchor="center")

clear_btn = CTkButton(master=frame1,text="Clear",corner_radius=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=clear)
clear_btn.place(relheight=0.08,relwidth=0.18,relx=0.35,rely=0.87,anchor="center")




ua_forms.resizable(False, False)
ua_forms.mainloop()