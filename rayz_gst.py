from tkinter import *
import customtkinter
from customtkinter import *

app = CTk()
message_1 = customtkinter.CTkLabel(app,text="Rayz_GST")
message_1.grid(row=0,column=0,columnspan = 2)


base_price = customtkinter.CTkEntry(app,placeholder_text="Enter the base product price:- ",width=200)
# base_price.insert(0,"")
base_price.grid(row = 1, column = 0,pady = 10)

gst_percentage = customtkinter.CTkEntry(app,placeholder_text="Enter the percentage of GST:- ",width=200)
gst_percentage.grid(row = 1, column = 1)

text_box_1 = customtkinter.CTkTextbox(app,border_width=2,width = 400,height=100)
# text_box_1.get("0.0","")
text_box_1.grid(row=3,column=0 , padx=10,pady=10,columnspan = 2)

def add_gst():
    gst_amt = (float(base_price.get()) * float(gst_percentage.get())) / 100
    final_price = float(base_price.get()) + gst_amt
    message = "GST Added amount:- " + str(final_price)
    text_box_1.insert("0.0",message)

def subtract_gst():
    gst_amt = float(base_price.get()) - (float(base_price.get()) * (100 / (100 + float(gst_percentage.get()))) / 100)
    final_price = float(base_price.get()) - gst_amt
    message = "GST subtracted amount:- " + str(final_price)
    text_box_1.insert("0.0",message)
    
Add_gst = customtkinter.CTkButton(app,text="Add GST",command= add_gst)
Add_gst.grid(row=4,column=0,pady=10)

subtract_gst = customtkinter.CTkButton(app,text="Subtract GST",command = subtract_gst)
subtract_gst.grid(row=4,column=1,pady=10)
app.mainloop()
