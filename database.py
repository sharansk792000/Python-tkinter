from tkinter import *

root = Tk()


head_label = Label(root, text="Restaurant Management System",background="lightblue",fg="white",width=42,padx=10,pady=30)
head_label.config(font=("Bold",32))
head_label.grid(row=0,column=0,columnspan=6,padx=10,pady=10)

main_frame_items = LabelFrame(root, text="", padx=5,pady=10,borderwidth=10)
main_frame_items.grid(row=1,column=0,columnspan=3,padx=(15,5),pady=10,sticky=W)

main_frame_price = LabelFrame(root, text="", padx=5,pady=20,borderwidth=10)
main_frame_price.grid(row=2,column=0,columnspan=3,padx=(15,5),pady=10,sticky=W)

main_frame_bill = LabelFrame(root, text="", padx=5,pady=10,borderwidth=10)
main_frame_bill.grid(row=1,rowspan=3,column=3,columnspan=6,padx=(0,5),pady=10,sticky=W+N)

main_frame_option = LabelFrame(root, text="", padx=5,pady=10,borderwidth=10)
main_frame_option.grid(row=1,rowspan=3,column=5,columnspan=7,padx=(5,12),pady=10,sticky=W+N)

drinks_frame = LabelFrame(main_frame_items, text="Drinks",borderwidth=5,padx=30,pady=30)
drinks_frame.grid(row=0,column=0,columnspan=2,padx=5,pady=10)

food_frame = LabelFrame(main_frame_items, text="Food",borderwidth=5,padx=30,pady=30)
food_frame.grid(row=0,column=2,columnspan=4,padx=(15,5),pady=5)


#DRINKS check box
drink_check_1 = Label(drinks_frame,text="Lassi",width=10,bg="lightblue")
drink_check_2 = Label(drinks_frame,text="Coffee",width=10,bg="lightblue")
drink_check_3 = Label(drinks_frame,text="Tea",width=10,bg="lightblue")
drink_check_4 = Label(drinks_frame,text="Juice",width=10,bg="lightblue")
drink_check_5 = Label(drinks_frame,text="Shakes",width=10,bg="lightblue")

drink_check_1.grid(row=0,column=0,padx=(0,10),sticky=W)
drink_check_2.grid(row=1,column=0,padx=(0,10),sticky=W)
drink_check_3.grid(row=2,column=0,padx=(0,10),sticky=W)
drink_check_4.grid(row=3,column=0,padx=(0,10),sticky=W)
drink_check_5.grid(row=4,column=0,padx=(0,10),sticky=W)

#DRINKS input
drinks_input_1 = Entry(drinks_frame,borderwidth=3,width=10)
drinks_input_2 = Entry(drinks_frame,borderwidth=3,width=10)
drinks_input_3 = Entry(drinks_frame,borderwidth=3,width=10)
drinks_input_4 = Entry(drinks_frame,borderwidth=3,width=10)
drinks_input_5 = Entry(drinks_frame,borderwidth=3,width=10)

drinks_input_1.grid(row=0,column=1,sticky=E)
drinks_input_2.grid(row=1,column=1,sticky=E)
drinks_input_3.grid(row=2,column=1,sticky=E)
drinks_input_4.grid(row=3,column=1,sticky=E)
drinks_input_5.grid(row=4,column=1,sticky=E)

#FOOD label
food_check_1 = Label(food_frame,text="Roti",width=10,bg="lightblue")
food_check_2 = Label(food_frame,text="Dal Makhni",width=10,bg="lightblue")
food_check_3 = Label(food_frame,text="Mutter Paneer",width=10,bg="lightblue")
food_check_4 = Label(food_frame,text="Paratha",width=10,bg="lightblue")
food_check_5 = Label(food_frame,text="Mix Veg",width=10,bg="lightblue")

food_check_1.grid(row=0,column=0,padx=(0,10),sticky=W)
food_check_2.grid(row=1,column=0,padx=(0,10),sticky=W)
food_check_3.grid(row=2,column=0,padx=(0,10),sticky=W)
food_check_4.grid(row=3,column=0,padx=(0,10),sticky=W)
food_check_5.grid(row=4,column=0,padx=(0,10),sticky=W)

#FOOD input
food_input_1 = Entry(food_frame,borderwidth=3,width=10)
food_input_2 = Entry(food_frame,borderwidth=3,width=10)
food_input_3 = Entry(food_frame,borderwidth=3,width=10)
food_input_4 = Entry(food_frame,borderwidth=3,width=10)
food_input_5 = Entry(food_frame,borderwidth=3,width=10)

food_input_1.grid(row=0,column=1,sticky=E)
food_input_2.grid(row=1,column=1,sticky=E)
food_input_3.grid(row=2,column=1,sticky=E)
food_input_4.grid(row=3,column=1,sticky=E)
food_input_5.grid(row=4,column=1,sticky=E)

#COST display
cost_drink = Label(main_frame_price,text="COST of Drinks",width=15,pady=5,background="lightblue").grid(row=0,column=0,padx=5)
cost_food = Label(main_frame_price,text="COST of Food",width=15,pady=5,background="lightblue").grid(row=1,column=0,padx=5)
service_charge = Label(main_frame_price,text="Service Charge",width=15,pady=5,background="lightblue").grid(row=2,column=0,padx=5)

cost_drink_input = Entry(main_frame_price,borderwidth=3,width=15).grid(row=0,column=1,padx=5,pady=5)
cost_food_input = Entry(main_frame_price,borderwidth=3,width=15).grid(row=1,column=1,padx=5,pady=5)
service_charge_input = Entry(main_frame_price,borderwidth=3,width=15).grid(row=2,column=1,padx=5,pady=5)


paid_tax = Label(main_frame_price,text="Paid Tax",width=15,pady=5,background="lightblue").grid(row=0,column=2,padx=(20,5))
sub_total = Label(main_frame_price,text="Sub Total",width=15,pady=5,background="lightblue").grid(row=1,column=2,padx=(20,5))
total_cost = Label(main_frame_price,text="Total Cost",width=15,pady=5,background="lightblue").grid(row=2,column=2,padx=(20,5))

paid_tax_input = Entry(main_frame_price,borderwidth=3,width=15).grid(row=0,column=3,padx=5,pady=5)
sub_total_input = Entry(main_frame_price,borderwidth=3,width=15).grid(row=1,column=3,padx=5,pady=5)
total_cost_input = Entry(main_frame_price,borderwidth=3,width=15).grid(row=2,column=3,padx=5,pady=5)


#CALCUATOR
cal_input = Entry(main_frame_bill,width=50,borderwidth=5)
cal_input.grid(row=0,column=0,columnspan=5,pady=(0,10),sticky=W)


#CALCULATOR function
def cal(number):
    c = cal_input.get()
    cal_input.delete(0, END)
    cal_input.insert(0, str(c)+str(number))

def button_add():
    global first_num
    global condition
    num = cal_input.get()
    first_num = int(num)
    condition = "add"
    cal_input.delete(0, END)

def button_sub():
    global first_num
    global condition
    num = cal_input.get()
    first_num = int(num)
    condition = "sub"
    cal_input.delete(0, END)

def button_mul():
    global first_num
    global condition
    num = cal_input.get()
    first_num = int(num)
    condition = "mul"
    cal_input.delete(0, END)

def button_div():
    global first_num
    global condition
    num = cal_input.get()
    first_num = int(num)
    condition = "div"
    cal_input.delete(0, END)

def button_equal():
    sec_num = cal_input.get()
    cal_input.delete(0, END)

    if condition == "add":
        cal_input.insert(0, first_num + int(sec_num))   

    if condition == "sub":
        cal_input.insert(0, first_num - int(sec_num))

    if condition == "mul":
        cal_input.insert(0, first_num * int(sec_num)) 

    if condition == "div":
        cal_input.insert(0, first_num / int(sec_num))
    
def button_clear():
    cal_input.delete(0, END)


input_1 = Button(main_frame_bill,text="1",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(1)).grid(row=3,column=2)
input_2 = Button(main_frame_bill,text="2",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(2)).grid(row=3,column=1)
input_3 = Button(main_frame_bill,text="3",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(3)).grid(row=3,column=0)
input_4 = Button(main_frame_bill,text="4",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(4)).grid(row=2,column=2)
input_5 = Button(main_frame_bill,text="5",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(5)).grid(row=2,column=1)
input_6 = Button(main_frame_bill,text="6",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(6)).grid(row=2,column=0)
input_7 = Button(main_frame_bill,text="7",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(7)).grid(row=1,column=2)
input_8 = Button(main_frame_bill,text="8",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(8)).grid(row=1,column=1)
input_9 = Button(main_frame_bill,text="9",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(9)).grid(row=1,column=0)
input_0 = Button(main_frame_bill,text="0",padx=30,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command=lambda: cal(0)).grid(row=4,column=0)

input_add = Button(main_frame_bill,text="+",padx=31,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command= button_add).grid(row=1,column=4)
input_sub = Button(main_frame_bill,text="-",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command= button_sub).grid(row=2,column=4)
input_mul = Button(main_frame_bill,text="*",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command= button_mul).grid(row=3,column=4)
input_div = Button(main_frame_bill,text="/",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED,command= button_div).grid(row=4,column=4)

input_eq = Button(main_frame_bill,text="=",padx=29,pady=9,fg="black",background="lightblue",borderwidth=2,relief=RAISED,command= button_equal).grid(row=4,column=2)
input_clear = Button(main_frame_bill,text="C",padx=29,pady=9,fg="black",background="violet",borderwidth=2,relief=RAISED,command= button_clear).grid(row=4,column=1)


#BILL generator
bill_generator = Label(main_frame_bill,text="Bill no. xxx    yyyy-mm-dd\n" + "========================\nItem(s)\t\tAmount\n========================",width=30,borderwidth=5,relief=RAISED)
bill_generator.config(font=("Courier",13))
bill_generator.grid(row=5,rowspan=8,column=0,columnspan=10,pady=(15,10))





#BUTTONS
total_button = Button(main_frame_option,text="Total",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED).grid(row=0,column=0,columnspan=2,padx=10,pady=10)
save_button = Button(main_frame_option,text="Save",padx=32,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED).grid(row=1,column=0,columnspan=2,padx=10,pady=10)
send_button = Button(main_frame_option,text="Send",padx=31,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED).grid(row=2,column=0,columnspan=2,padx=10,pady=10)
exit_button = Button(main_frame_option,text="Exit",padx=33,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED, command=root.quit).grid(row=3,column=0,columnspan=2,padx=10,pady=10)
update_button = Button(main_frame_option,text="Update",padx=23,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED).grid(row=4,column=0,columnspan=2,padx=10,pady=10)
reset_button = Button(main_frame_option,text="Reset",padx=29,pady=9,fg="white",background="violet",borderwidth=2,relief=RAISED).grid(row=5,column=0,columnspan=2,padx=10,pady=10)



root.mainloop()
