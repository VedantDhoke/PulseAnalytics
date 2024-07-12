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
    alb_entry.delete(0, END)
    glb_entry.delete(0, END)
    tsp_entry.delete(0, END)
    bbt_entry.delete(0, END)
    alp_entry.delete(0, END)
    ast_entry.delete(0, END)

def submit():
    lft_forms.destroy()

lft_forms = CTk()
lft_forms.title("PulseAnalytics")
x = (lft_forms.winfo_screenwidth() - 650) // 2
y = (lft_forms.winfo_screenheight() - 700) // 2
lft_forms.geometry(f"650x700+{x}+{y}")
lft_forms.configure(bg="#000000")

frame1 = CTkFrame(master=lft_forms, fg_color="#96EFFF", corner_radius=0, width=650,height=700)
frame1.place(x=0, y=0)

title_label = CTkLabel(master=frame1, text="lft Form", font=CTkFont('Microsoft YaHei UI Light',35,"bold",underline="true"),text_color="#000000")
title_label.place(relx=0.5, rely=0.08,anchor="center")

date_label = CTkLabel(master=frame1, text="Date:", font=CTkFont('Kanit Regular',20),text_color="#000000")
date_label.place(relx=0.1,rely=0.18)
date_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="DD/MM/YYYY",text_color="#000000")
date_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.18)

alb_label = CTkLabel(master=frame1, text="Albumin:", font=CTkFont('Kanit Regular',20),text_color="#000000")
alb_label.place(relx=0.1,rely=0.28)
alb_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
alb_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.28)

glb_label = CTkLabel(master=frame1, text="Globulin:", font=CTkFont('Kanit Regular',20),text_color="#000000")
glb_label.place(relx=0.1,rely=0.38)
glb_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
glb_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.38)

tsp_label = CTkLabel(master=frame1, text="Total Serum Protein:", font=CTkFont('Kanit Regular',20),text_color="#000000")
tsp_label.place(relx=0.1,rely=0.48)
tsp_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
tsp_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.48)

bbt_label = CTkLabel(master=frame1, text="Bilrubin Total:", font=CTkFont('Kanit Regular',20),text_color="#000000")
bbt_label.place(relx=0.1,rely=0.58)
bbt_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
bbt_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.58)

alp_label = CTkLabel(master=frame1, text="ALP:", font=CTkFont('Kanit Regular',20),text_color="#000000")
alp_label.place(relx=0.1,rely=0.68)
alp_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
alp_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.68)

ast_label = CTkLabel(master=frame1, text="AST:", font=CTkFont('Kanit Regular',20),text_color="#000000")
ast_label.place(relx=0.1,rely=0.78)
ast_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="tbd",text_color="#000000")
ast_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.78)


submit_btn = CTkButton(master=frame1,text="Submit",corner_radius=30,fg_color="#5FBDFF",hover_color="#7B66FF",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=submit)
submit_btn.place(relheight=0.06,relwidth=0.19,relx=0.65,rely=0.92,anchor="center")

clear_btn = CTkButton(master=frame1,text="Clear",corner_radius=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=clear)
clear_btn.place(relheight=0.06,relwidth=0.18,relx=0.35,rely=0.92,anchor="center")




lft_forms.resizable(False, False)
lft_forms.mainloop()