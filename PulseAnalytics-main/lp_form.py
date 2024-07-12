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
    chl_entry.delete(0, END)
    tgc_entry.delete(0, END)
    hdlc_entry.delete(0, END)
    ldlc_entry.delete(0, END)
    vldl_entry.delete(0, END)
    nhdlc_entry.delete(0, END)

def submit():
    lp_forms.destroy()

lp_forms = CTk()
lp_forms.title("PulseAnalytics")
x = (lp_forms.winfo_screenwidth() - 650) // 2
y = (lp_forms.winfo_screenheight() - 700) // 2
lp_forms.geometry(f"650x700+{x}+{y}")
lp_forms.configure(bg="#000000")

frame1 = CTkFrame(master=lp_forms, fg_color="#96EFFF", corner_radius=0, width=650,height=700)
frame1.place(x=0, y=0)

title_label = CTkLabel(master=frame1, text="LP Form", font=CTkFont('Microsoft YaHei UI Light',35,"bold",underline="true"),text_color="#000000")
title_label.place(relx=0.5, rely=0.08,anchor="center")

date_label = CTkLabel(master=frame1, text="Date:", font=CTkFont('Kanit Regular',20),text_color="#000000")
date_label.place(relx=0.1,rely=0.18)
date_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="DD/MM/YYYY",text_color="#000000")
date_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.18)

chl_label = CTkLabel(master=frame1, text="Cholesterol:", font=CTkFont('Kanit Regular',20),text_color="#000000")
chl_label.place(relx=0.1,rely=0.28)
chl_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
chl_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.28)

tgc_label = CTkLabel(master=frame1, text="Triglycerides:", font=CTkFont('Kanit Regular',20),text_color="#000000")
tgc_label.place(relx=0.1,rely=0.38)
tgc_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
tgc_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.38)

hdlc_label = CTkLabel(master=frame1, text="HDL cholesterol:", font=CTkFont('Kanit Regular',20),text_color="#000000")
hdlc_label.place(relx=0.1,rely=0.48)
hdlc_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
hdlc_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.48)

ldlc_label = CTkLabel(master=frame1, text="LDL cholesterol:", font=CTkFont('Kanit Regular',20),text_color="#000000")
ldlc_label.place(relx=0.1,rely=0.58)
ldlc_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
ldlc_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.58)

vldl_label = CTkLabel(master=frame1, text="VLDL cholesterol:", font=CTkFont('Kanit Regular',20),text_color="#000000")
vldl_label.place(relx=0.1,rely=0.68)
vldl_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="%d",text_color="#000000")
vldl_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.68)

nhdlc_label = CTkLabel(master=frame1, text="Non-HDL cholesterol:", font=CTkFont('Kanit Regular',20),text_color="#000000")
nhdlc_label.place(relx=0.1,rely=0.78)
nhdlc_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
nhdlc_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.78)


submit_btn = CTkButton(master=frame1,text="Submit",corner_radius=30,fg_color="#5FBDFF",hover_color="#7B66FF",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=submit)
submit_btn.place(relheight=0.06,relwidth=0.19,relx=0.65,rely=0.92,anchor="center")

clear_btn = CTkButton(master=frame1,text="Clear",corner_radius=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=clear)
clear_btn.place(relheight=0.06,relwidth=0.18,relx=0.35,rely=0.92,anchor="center")




lp_forms.resizable(False, False)
lp_forms.mainloop()