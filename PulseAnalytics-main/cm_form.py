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
    wbc_entry.delete(0, END)
    plt_entry.delete(0, END)
    ast_entry.delete(0, END)
    ldlch_entry.delete(0, END)
    tg_entry.delete(0, END)
    hmg_entry.delete(0, END)

def submit():
    cm_forms.destroy()

cm_forms = CTk()
cm_forms.title("PulseAnalytics")
x = (cm_forms.winfo_screenwidth() - 650) // 2
y = (cm_forms.winfo_screenheight() - 700) // 2
cm_forms.geometry(f"650x700+{x}+{y}")
cm_forms.configure(bg="#000000")

frame1 = CTkFrame(master=cm_forms, fg_color="#96EFFF", corner_radius=0, width=650,height=700)
frame1.place(x=0, y=0)

title_label = CTkLabel(master=frame1, text="CM Form", font=CTkFont('Microsoft YaHei UI Light',35,"bold",underline="true"),text_color="#000000")
title_label.place(relx=0.5, rely=0.08,anchor="center")

date_label = CTkLabel(master=frame1, text="Date:", font=CTkFont('Kanit Regular',20),text_color="#000000")
date_label.place(relx=0.1,rely=0.18)
date_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="DD/MM/YYYY",text_color="#000000")
date_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.18)

wbc_label = CTkLabel(master=frame1, text="WBC count:", font=CTkFont('Kanit Regular',20),text_color="#000000")
wbc_label.place(relx=0.1,rely=0.28)
wbc_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
wbc_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.28)

plt_label = CTkLabel(master=frame1, text="Platelets:", font=CTkFont('Kanit Regular',20),text_color="#000000")
plt_label.place(relx=0.1,rely=0.38)
plt_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
plt_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.38)

ast_label = CTkLabel(master=frame1, text="AST level:", font=CTkFont('Kanit Regular',20),text_color="#000000")
ast_label.place(relx=0.1,rely=0.48)
ast_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
ast_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.48)

ldlch_label = CTkLabel(master=frame1, text="LDL cholesterol:", font=CTkFont('Kanit Regular',20),text_color="#000000")
ldlch_label.place(relx=0.1,rely=0.58)
ldlch_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
ldlch_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.58)

tg_label = CTkLabel(master=frame1, text="Triglycerides:", font=CTkFont('Kanit Regular',20),text_color="#000000")
tg_label.place(relx=0.1,rely=0.68)
tg_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
tg_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.68)

hmg_label = CTkLabel(master=frame1, text="Heamoglobin level:", font=CTkFont('Kanit Regular',20),text_color="#000000")
hmg_label.place(relx=0.1,rely=0.78)
hmg_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
hmg_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.78)


submit_btn = CTkButton(master=frame1,text="Submit",corner_radius=30,fg_color="#5FBDFF",hover_color="#7B66FF",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=submit)
submit_btn.place(relheight=0.06,relwidth=0.19,relx=0.65,rely=0.92,anchor="center")

clear_btn = CTkButton(master=frame1,text="Clear",corner_radius=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=clear)
clear_btn.place(relheight=0.06,relwidth=0.18,relx=0.35,rely=0.92,anchor="center")




cm_forms.resizable(False, False)
cm_forms.mainloop()