from tkinter import *
import customtkinter
from customtkinter import *

app = CTk()

message_1 = customtkinter.CTkLabel(app,text="Rayz_GST")
message_1.grid(row=0,column=0)

text_box_1 = customtkinter.CTkTextbox(app,border_width=2)
# text_box_1.get("0.0","")
text_box_1.grid(row=1,column=0)

app.mainloop()
