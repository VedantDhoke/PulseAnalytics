from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label
import pymysql

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\LENOVO\Downloads\PulseAnalytics-main\PulseAnalytics-main\Assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def fetch_dates_from_database():
    conn = pymysql.connect(host='localhost', user='root', password='P@ssw0rd', database='pulseanalytics')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT DateColumn FROM cbc")  # Fetch unique dates from the table
    ids = [emp_id[0] for emp_id in cursor.fetchall()]  # Extract dates from the fetched data
    conn.close()
    return ids

def fetch_row_from_database(date_value):
    conn = pymysql.connect(host='localhost', user='root', password='P@ssw0rd', database='pulseanalytics')
    cursor = conn.cursor()
    cursor.execute("select Haemoglobin, RBC, WBC, Platelet, Hematocrit, MCV from cbc where DateColumn=%s", (date_value,))
    row = cursor.fetchone()  # Fetch the first row that matches the date
    conn.close()
    return row

def archive():
    report_compare.destroy()
    import reports

def on_date_selected1():
    selected_date = date_var1.get()
    row = fetch_row_from_database(selected_date)
    if row:
        for i, value in enumerate(row[0:]):
            text_fields[0][i].configure(state='normal')
            text_fields[0][i].delete(0, END)
            if(value==None):
                value=0
            text_fields[0][i].insert(END, str(value))
            text_fields[0][i].configure(state='readonly')
            
    for a in range(0,6):
        if(float(text_fields[0][a].get()) < float(text_fields[1][a].get())):
            text_fields[1][a].configure(border_width=1, border_color="#00B700", text_color="#00B700")
            text_fields[0][a].configure(border_width=1, border_color="#FF0000", text_color="#FF0000")
        elif(float(text_fields[0][a].get()) > float(text_fields[1][a].get())):
            text_fields[1][a].configure(border_width=1, border_color="#FF0000", text_color="#FF0000")
            text_fields[0][a].configure(border_width=1, border_color="#00B700", text_color="#00B700")
        elif(float(text_fields[0][a].get()) == float(text_fields[1][a].get())):
            text_fields[1][a].configure(border_width=0, text_color="#000000")
            text_fields[0][a].configure(border_width=0, text_color="#000000")
            
def on_date_selected2():
    selected_date = date_var2.get()
    row = fetch_row_from_database(selected_date)
    if row:
        for i, value in enumerate(row[0:]):
            text_fields[1][i].configure(state='normal')
            text_fields[1][i].delete(0, END)
            if(value==None):
                value=0
            text_fields[1][i].insert(END, str(value))
            text_fields[1][i].configure(state='readonly')
    
    for a in range(0,6):
        if(float(text_fields[0][a].get()) < float(text_fields[1][a].get())):
            text_fields[1][a].configure(border_width=1, border_color="#00B700", text_color="#00B700")
            text_fields[0][a].configure(border_width=1, border_color="#FF0000", text_color="#FF0000")
        elif(float(text_fields[0][a].get()) > float(text_fields[1][a].get())):
            text_fields[1][a].configure(border_width=1, border_color="#FF0000", text_color="#FF0000")
            text_fields[0][a].configure(border_width=1, border_color="#00B700", text_color="#00B700")
        elif(float(text_fields[0][a].get()) == float(text_fields[1][a].get())):
            text_fields[1][a].configure(border_width=0, text_color="#000000")
            text_fields[0][a].configure(border_width=0, text_color="#000000")

units=["10^6/µL","10^3/µL","10^3/µL","g/dL","%","fL"]


report_compare = CTk()
report_compare.title("PulseAnalytics")
x = (report_compare.winfo_screenwidth() - 900) // 2
y = (report_compare.winfo_screenheight() - 750) // 2
report_compare.geometry(f"900x750+{x}+{y}")
report_compare.configure(bg="#000000")

frame1 = CTkFrame(master=report_compare, fg_color="#EBEEF6", corner_radius=0, width=900,height=750)
frame1.place(x=0, y=0)

back_btn = CTkButton(master=frame1,text="Back",corner_radius=30,fg_color="transparent",hover_color="#FF2D3F",border_width=2,border_color="black",width=150,height=60,font=CTkFont('Kanit Regular',15),text_color="#000000",command=archive)
back_btn.place(relheight=0.04,relwidth=0.11,relx=0.03,rely=0.03)

title = CTkLabel(master=frame1, text="Report Comparison", font=CTkFont('Microsoft YaHei UI Light',30,"bold",underline="true"), text_color="#000000")
title.place(relx=0.5, rely=0.08,anchor='center')

left_frame = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20)
left_frame.place(relheight=0.055,relwidth=0.2,relx=0.24,rely=0.2,anchor='center')
date_var1 = StringVar()
dates1 = fetch_dates_from_database()
date_dropdown1 = CTkComboBox(master=left_frame, variable=date_var1, values=[str(i) for i in dates1], border_width=0, dropdown_fg_color="#FFFFFF", dropdown_hover_color="#EBEEF6",dropdown_text_color="#000000", fg_color="#FFFFFF", corner_radius=10, button_color="#FFFFFF", button_hover_color="#EBEEF6", text_color="#000000")
date_dropdown1.place(relx=0.5, rely=0.5, anchor=CENTER)
date_var1.trace('w', lambda *args: on_date_selected1())

right_frame = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20)
right_frame.place(relheight=0.055,relwidth=0.2,relx=0.74,rely=0.2,anchor='center')
date_var2 = StringVar()
dates2 = fetch_dates_from_database()
date_dropdown2 = CTkComboBox(master=right_frame, variable=date_var2, values=[str(i) for i in dates2], border_width=0, dropdown_fg_color="#FFFFFF", dropdown_hover_color="#EBEEF6",dropdown_text_color="#000000", fg_color="#FFFFFF", corner_radius=10, button_color="#FFFFFF", button_hover_color="#EBEEF6", text_color="#000000")
date_dropdown2.place(relx=0.5, rely=0.5, anchor=CENTER)
date_var2.trace('w', lambda *args: on_date_selected2())

rows = 2
cols = 6
text_fields = [['' for j in range(cols)] for i in range(rows)]

for i in range(rows):
    for j in range(cols):
        text_field = CTkEntry(master=frame1, border_width=0, fg_color="#FFFFFF", corner_radius=20)
        text_field.place(relx=0.25 if i==0 else 0.75, rely=0.3 + (j * 0.09), relheight=0.05, relwidth=0.25, anchor=CENTER)
        text_fields[i][j] = text_field 

rbc_label = CTkLabel(master=frame1,text="RBC Count",font=CTkFont('Kanit Regular', 20), text_color="#000000")
rbc_label.place(relx=0.5,rely=0.3,anchor='center')

wbc_label = CTkLabel(master=frame1,text="WBC Count",font=CTkFont('Kanit Regular', 20), text_color="#000000")
wbc_label.place(relx=0.5,rely=0.39,anchor='center')

plt_label = CTkLabel(master=frame1,text="Platelet Level",font=CTkFont('Kanit Regular', 20), text_color="#000000")
plt_label.place(relx=0.5,rely=0.48,anchor='center')

hmg_label = CTkLabel(master=frame1,text="Heamoglobin Level",font=CTkFont('Kanit Regular', 20), text_color="#000000")
hmg_label.place(relx=0.5,rely=0.57,anchor='center')

hmt_label = CTkLabel(master=frame1,text="Hematocrit Level",font=CTkFont('Kanit Regular', 20), text_color="#000000")
hmt_label.place(relx=0.5,rely=0.66,anchor='center')

mcv_label = CTkLabel(master=frame1,text="MCV Level",font=CTkFont('Kanit Regular', 20), text_color="#000000")
mcv_label.place(relx=0.5,rely=0.75,anchor='center')

bottom_frame = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20)
bottom_frame.place(relheight=0.16,relwidth=0.9,relx=0.5,rely=0.9,anchor='center')

range_label1 = CTkLabel(master=bottom_frame,text="• The field being green denotes an increase in the value of the reading.",font=CTkFont('Kanit Regular', 15), text_color="#00B700")
range_label1.place(relx=0.04, rely=0.1)

range_label2 = CTkLabel(master=bottom_frame,text="• The field being red denotes a decrease in the value of the reading.",font=CTkFont('Kanit Regular', 15), text_color="#FF0000")
range_label2.place(relx=0.04, rely=0.4)

range_label3 = CTkLabel(master=bottom_frame,text="• The field being black denotes no change in the value of the reading.",font=CTkFont('Kanit Regular', 15), text_color="#000000")
range_label3.place(relx=0.04, rely=0.7)

report_compare.mainloop()