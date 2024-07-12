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

bbc_graph = CTk()
bbc_graph.title("PulseAnalytics")
x = (bbc_graph.winfo_screenwidth() - 1250) // 2
y = (bbc_graph.winfo_screenheight() - 768) // 2
bbc_graph.geometry(f"1250x750+{x}+{y}")
bbc_graph.configure(bg="#000000")

frame1 = CTkScrollableFrame(master=bbc_graph, fg_color="#EBEEF6", corner_radius=0, width=1250,height=750)
frame1.place(relx=0, rely=0)


graphframe1 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe1.grid(row=0, column=0, pady=20, padx=12)

urea_label = CTkLabel(master=graphframe1, text="Urea:", font=CTkFont('Kanit Regular',30),text_color="#000000")
urea_label.place(relx=0.5,rely=0.1,anchor='center')

conn = pymysql.connect(host='localhost', user='root', password='P@ssw0rd', database='pulseanalytics')
query = "SELECT Urea, DateColumn FROM bbc"
data = pd.read_sql(query, conn)

data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Urea'], marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Urea')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe1)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe2 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe2.grid(row=0, column=1, pady=20, padx=12)

creatinine_label = CTkLabel(master=graphframe2, text="Creatinine:", font=CTkFont('Kanit Regular',30),text_color="#000000")
creatinine_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT Creatinine, DateColumn FROM bbc"
data = pd.read_sql(query, conn)
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Creatinine'], marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Creatinine')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe2)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe3 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe3.grid(row=1, column=0, pady=20, padx=12)

sodium_label = CTkLabel(master=graphframe3, text="Sodium:", font=CTkFont('Kanit Regular',30),text_color="#000000")
sodium_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT Sodium, DateColumn FROM bbc"
data = pd.read_sql(query, conn)
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Sodium'], marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Sodium')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe3)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe4 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe4.grid(row=1, column=1, pady=20, padx=12)

potassium_label = CTkLabel(master=graphframe4, text="Potassium:", font=CTkFont('Kanit Regular',30),text_color="#000000")
potassium_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT Potassium, DateColumn FROM bbc"
data = pd.read_sql(query, conn)
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Potassium'], marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Potassium')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe4)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe5 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe5.grid(row=2, column=0, pady=20, padx=12)

uric_acid_label = CTkLabel(master=graphframe5, text="Uric Acid :", font=CTkFont('Kanit Regular',30),text_color="#000000")
uric_acid_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT Uric_acid, DateColumn FROM bbc"
data = pd.read_sql(query, conn)
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Uric_acid'], color='blue' ,marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Uric_acid')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe5)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


graphframe6 = CTkFrame(master=frame1, fg_color="#FFFFFF", corner_radius=20, height=400,width=600)
graphframe6.grid(row=2, column=1, pady=20, padx=12)

total_protein_label = CTkLabel(master=graphframe6, text="Total Protein :", font=CTkFont('Kanit Regular',30),text_color="#000000")
total_protein_label.place(relx=0.5,rely=0.1,anchor='center')

query = "SELECT Total_protein, DateColumn FROM bbc"
data = pd.read_sql(query, conn)
conn.close()
data['DateColumn'] = pd.to_datetime(data['DateColumn'])

fig = Figure(figsize=(4.5, 3.5), dpi=100)
ax = fig.add_subplot(111)
ax.plot(data['DateColumn'], data['Total_protein'], color='blue' ,marker='o', linestyle='-')
ax.set_xlabel('Time')
ax.set_ylabel('Total_protein')
ax.legend()
ax.grid(True)
canvas = FigureCanvasTkAgg(fig, master=graphframe6)
canvas.draw()
canvas.get_tk_widget().place(relheight=0.8,relwidth=0.9,relx=0.5,rely=0.55,anchor='center')


bbc_graph.resizable(False, False)
bbc_graph.mainloop()