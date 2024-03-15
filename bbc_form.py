from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label
import pymysql

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LENOVO\Downloads\PulseAnalytics-main\PulseAnalytics-main\Assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def connect_database():
    if date_entry.get()=='' or urea_entry.get()=='' or crt_entry.get()=='' or na_entry.get()=='' or k_entry.get()=='' or uric_entry.get()=='' or prt_entry.get()=='':
        messagebox.showerror('Error','All Fields Are Required')
    elif (not all(is_numeric(entry.get()) for entry in (urea_entry, crt_entry, na_entry, k_entry, uric_entry, prt_entry))):
        messagebox.showerror('Error', 'All Fields Must Contain Numeric Values')
            
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='P@ssw0rd')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return
        query = 'use PulseAnalytics'
        mycursor.execute(query)
        
        query='insert into bbc(DateColumn, Urea, Creatinine, Sodium, Potassium, Uric_acid, Total_protein ) values(%s,%s,%s,%s,%s,%s,%s)'   
        mycursor.execute(query,(date_entry.get(),urea_entry.get(),crt_entry.get(),na_entry.get(),k_entry.get(),uric_entry.get(),prt_entry.get()))
        con.commit()
        con.close()
        messagebox.showinfo('Success','Form Is Filled Successfully')
        clear()
        import dashboard
    
def clear():
    date_entry.delete(0, END)
    urea_entry.delete(0, END)
    crt_entry.delete(0, END)
    na_entry.delete(0, END)
    k_entry.delete(0, END)
    uric_entry.delete(0, END)
    prt_entry.delete(0, END)

def submit():
    bbc_forms.destroy()

bbc_forms = CTk()
bbc_forms.title("PulseAnalytics")
x = (bbc_forms.winfo_screenwidth() - 650) // 2
y = (bbc_forms.winfo_screenheight() - 700) // 2
bbc_forms.geometry(f"650x700+{x}+{y}")
bbc_forms.configure(bg="#000000")

frame1 = CTkFrame(master=bbc_forms, fg_color="#96EFFF", corner_radius=0, width=650,height=700)
frame1.place(x=0, y=0)

title_label = CTkLabel(master=frame1, text="BBC Form", font=CTkFont('Microsoft YaHei UI Light',35,"bold",underline="true"))
title_label.place(relx=0.5, rely=0.08,anchor="center")

date_label = CTkLabel(master=frame1, text="Date:", font=CTkFont('Kanit Regular',20))
date_label.place(relx=0.1,rely=0.18)
date_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="YYYY/MM/DD")
date_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.18)

urea_label = CTkLabel(master=frame1, text="Urea:", font=CTkFont('Kanit Regular',20))
urea_label.place(relx=0.1,rely=0.28)
urea_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="10^6/µL")
urea_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.28)

crt_label = CTkLabel(master=frame1, text="Creatinine:", font=CTkFont('Kanit Regular',20))
crt_label.place(relx=0.1,rely=0.38)
crt_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mg/dL")
crt_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.38)

na_label = CTkLabel(master=frame1, text="Sodium:", font=CTkFont('Kanit Regular',20))
na_label.place(relx=0.1,rely=0.48)
na_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mEq/L")
na_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.48)

k_label = CTkLabel(master=frame1, text="Hemoglobin Level:", font=CTkFont('Kanit Regular',20))
k_label.place(relx=0.1,rely=0.58)
k_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="mEq/L")
k_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.58)

uric_label = CTkLabel(master=frame1, text="Uric acid:", font=CTkFont('Kanit Regular',20))
uric_label.place(relx=0.1,rely=0.68)
uric_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="%")
uric_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.68)

prt_label = CTkLabel(master=frame1, text="Total Protein:", font=CTkFont('Kanit Regular',20))
prt_label.place(relx=0.1,rely=0.78)
prt_entry = CTkEntry(master=frame1,corner_radius=12,fg_color="#FFFFFF",border_width=0,placeholder_text="g/dL")
prt_entry.place(relheight=0.05,relwidth=0.5,relx=0.4,rely=0.78)


submit_btn = CTkButton(master=frame1,text="Submit",corner_radius=30,fg_color="#5FBDFF",hover_color="#7B66FF",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=connect_database)
submit_btn.place(relheight=0.06,relwidth=0.19,relx=0.65,rely=0.92,anchor="center")

clear_btn = CTkButton(master=frame1,text="Clear",corner_radius=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',20),text_color="#000000",command=clear)
clear_btn.place(relheight=0.06,relwidth=0.18,relx=0.35,rely=0.92,anchor="center")




bbc_forms.resizable(False, False)
bbc_forms.mainloop()