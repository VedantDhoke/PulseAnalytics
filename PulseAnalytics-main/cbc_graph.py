from customtkinter import *
from pathlib import Path
from tkinter import *
from tkinter import messagebox, Toplevel, Label
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pymysql  # Assuming you're using SQL Server, adjust accordingly for other databases
import pandas as pd

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Lenovo\Desktop\Mini Project f\assets")

cbc_graph = CTk()
cbc_graph.title("PulseAnalytics")
x = (cbc_graph.winfo_screenwidth() - 1250) // 2
y = (cbc_graph.winfo_screenheight() - 768) // 2
cbc_graph.geometry(f"1250x750+{x}+{y}")
cbc_graph.configure(bg="#000000")

frame1 = CTkScrollableFrame(master=cbc_graph, fg_color="#EBEEF6", corner_radius=0, width=1250,height=750)
frame1.place(relx=0, rely=0)


graphframe1 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe1.grid(row=0, column=0, pady=20, padx=12)

hmg_label = CTkLabel(master=graphframe1, text="Haemoglobin:", font=CTkFont('Kanit Regular',30),text_color="#000000")
hmg_label.place(relx=0.5,rely=0.1,anchor='center')

conn = pymysql.connect(host='localhost', user='root', password='P@ssw0rd', database='pulseanalytics')
query = "SELECT Haemoglobin, DateColumn FROM cbc"
data = pd.read_sql(query, conn)

data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Haemoglobin'], marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Haemoglobin')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe1)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe2 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe2.grid(row=0, column=1, pady=20, padx=12)

rbc_label = CTkLabel(master=graphframe2, text="RBC count:", font=CTkFont('Kanit Regular',30),text_color="#000000")
rbc_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT RBC, DateColumn FROM cbc"
data = pd.read_sql(query, conn)
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['RBC'], marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('RBC')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe2)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe3 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe3.grid(row=1, column=0, pady=20, padx=12)

wbc_label = CTkLabel(master=graphframe3, text="WBC count:", font=CTkFont('Kanit Regular',30),text_color="#000000")
wbc_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT WBC, DateColumn FROM cbc"
data = pd.read_sql(query, conn)
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['WBC'], marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('WBC')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe3)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe4 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe4.grid(row=1, column=1, pady=20, padx=12)

Platelet_label = CTkLabel(master=graphframe4, text="Platelet count:", font=CTkFont('Kanit Regular',30),text_color="#000000")
Platelet_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT Platelet, DateColumn FROM cbc"
data = pd.read_sql(query, conn)
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Platelet'], marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Platelet')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe4)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe5 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe5.grid(row=2, column=0, pady=20, padx=12)

hematocrit_label = CTkLabel(master=graphframe5, text="Hematocrit :", font=CTkFont('Kanit Regular',30),text_color="#000000")
hematocrit_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT Hematocrit, DateColumn FROM cbc"
data = pd.read_sql(query, conn)
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Hematocrit'], color='blue' ,marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Hematocrit')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe5)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe6 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe6.grid(row=2, column=1, pady=20, padx=12)

MCV_label = CTkLabel(master=graphframe6, text="MCV :", font=CTkFont('Kanit Regular',30),text_color="#000000")
MCV_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT MCV, DateColumn FROM cbc"
data = pd.read_sql(query, conn)
conn.close()
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['MCV'], color='blue' ,marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('MCV')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe6)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


cbc_graph.resizable(False, False)
cbc_graph.mainloop()