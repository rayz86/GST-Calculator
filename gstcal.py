#Python code to calculate GST on a product
#Author: Rayyan Shaikh

def switch(op):
    if op == 1:
        gst_add()
    elif op == 2:
        gst_sub()
    else:
        print("Bad Input")

def gst_add():
    gst_amt = (base_price * gst) / 100
    final_price = base_price + gst_amt
    print("GST added amount:", final_price)

def gst_sub():
    gst_amt = base_price - (base_price * (100 / (100 + gst)) / 100)
    final_price = base_price - gst_amt
    print("GST subtracted amount:", final_price)

base_price = float(input("Enter the base product price: "))
gst = float(input("Enter the percentage of GST: "))
op = int(input("1) Add GST 2) Subtract GST: "))
switch(op)
