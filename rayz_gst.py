from tkinter import *
import customtkinter
from customtkinter import *

app = CTk()
app.title("GST CALCULATOR")
app.iconbitmap("./image/rayz.ico")
user = CTkFrame(app)
user.pack(padx=20, pady=20)

message_1 = customtkinter.CTkLabel(user,text="Rayz_GST",font=("Terminal", 25,"bold"),text_color="#ff8040")
message_1.grid(row=0,column=0,columnspan = 2,pady=10)


base_price = customtkinter.CTkEntry(user,placeholder_text="Enter the base product price:- ",width=200)
base_price.grid(row = 1, column = 0,pady = 10,padx=10)

gst_percentage = customtkinter.CTkEntry(user,placeholder_text="Enter the percentage of GST:- ",width=200)
gst_percentage.grid(row = 1, column = 1,padx=10)

def add_gst():    
    text_box_1 = customtkinter.CTkTextbox(user,border_width=2,width = 400,height=30,text_color="#00ff00")
    text_box_1.grid(row=3,column=0 , padx=10,pady=10,columnspan = 2)
    text_box_1.delete("0.0",customtkinter.END)
    gst_amt = (float(base_price.get()) * float(gst_percentage.get())) / 100
    final_price = float(base_price.get()) + gst_amt
    message = f"GST Added amount:- {final_price}" 
    text_box_1.insert("0.0",message)

def subtract_gst():
    text_box_1 = customtkinter.CTkTextbox(user,border_width=2,width = 400,height=30,text_color="#ff3030")
    text_box_1.grid(row=3,column=0 , padx=10,pady=10,columnspan = 2)
    text_box_1.delete("0.0",customtkinter.END)
    gst_amt = float(base_price.get()) - (float(base_price.get()) * (100 / (100 + float(gst_percentage.get()))) / 100)
    final_price = float(base_price.get()) - gst_amt
    message = f"GST subtracted amount:- {final_price}"
    text_box_1.insert("0.0",message)
    
Add_gst = customtkinter.CTkButton(user,text="Add GST",command= add_gst,fg_color="#00ff00",text_color="#000000")
Add_gst.grid(row=4,column=0,pady=10)

subtract_gst = customtkinter.CTkButton(user,text="Subtract GST",command = subtract_gst,fg_color="#ff4444",text_color="#000000")
subtract_gst.grid(row=4,column=1,pady=10)
app.mainloop()
