from tkinter import *
from fpdf import FPDF
from datetime import date, datetime


total = 0
Order = [""]*100000
#priceList = [529,529,529,569,569,569,419,469,69]
price = [0] *100000
noOfHits = -1
currentPrice = 0
discount = 0
noOfItems = [0]*100000

def display():
    global noOfHits
    global price
    global Order
    global noOfItems
    noOfHits = noOfHits + 1
    global total
    
    i = 0
    while(i<=noOfHits):
        temp = price[i] * noOfItems[i]
        total = total + temp
        i = i + 1

    global discount
    
    if(total>1000 and total<=2000): discount = 0.05 * total
    elif(total>2000 and total<=3000): discount = 0.1 * total
    elif(total>3000): discount = 0.15 * total

    finalAmt = total - discount
    txt1 = "Customer's Name : " + str(entryBox1.get())
    txt2 = "Mobile No. : " + str(entryBox2.get())
    txt3 = "Email ID : " + str(entryBox3.get())
    txt4 = "Order Total : " + str(int(total))
    txt5 = "Discount Amount : " + str(int(discount))
    txt6 = "Final Amount to be paid : " + str(int(finalAmt))

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times",'BIU',size = 35)
    pdf.cell(200,20,txt="Pizza Hut Bill Receipt",ln=1,align="C")
    pdf.set_font("Times",'I',size = 15)
    pdf.cell(200,10,txt=txt1,ln=3,align="L")
    pdf.cell(200,10,txt=txt2,ln=4,align="L")
    pdf.cell(200,10,txt=txt3,ln=5,align="L")
    pdf.cell(200,10,txt=txt4,ln=6,align="L")
    pdf.cell(200,10,txt=txt5,ln=7,align="L")
    pdf.cell(200,10,txt=txt6,ln=9,align="L")
    
    pdf.cell(200,30,txt="     ",ln=13,align="L")

    pdf.set_font("Times",'BI',size = 22)
    pdf.cell(200,10,txt="Order & Price      :      No of Items :-",ln=15,align="L")
    pdf.set_font("Times",'I',size = 15)
    j = 0
    while(j<noOfHits):
        textPrint = Order[j] + "  ------->   " + str(noOfItems[j]) 
        pdf.cell(200,10,txt=textPrint,ln=18,align="L")
        j = j + 1

    pdf.output("Bill.pdf")
    
def addToOrder():
    global noOfHits
    global Order
    global price
    global currentPrice
        
    choice = msg.get()
    noOfHits = noOfHits + 1

    noOfItems[noOfHits] = int(entryBox4.get())
    
    Order[noOfHits] = choice

    if(choice=="Country Feast Pizza : Rs 529"): currentPrice = 529
    elif(choice=="Farmers Pick Pizza : Rs 529"): currentPrice = 529
    elif(choice=="Tandoori Paneer Pizza : Rs 529"): currentPrice = 529
    elif(choice=="Chicken Sausage n Tikka Pizza : Rs 569"): currentPrice = 569
    elif(choice=="Chicken Tikka Pizza : Rs 569"): currentPrice = 569
    elif(choice=="Smoked Chicken Pizza : Rs 569"): currentPrice = 569
    elif(choice=="Double Cheese Pizza : Rs 419"): currentPrice = 419
    elif(choice=="Spiced Chicken Meatballs Pizza : Rs 469"): currentPrice = 469
    elif(choice=="Coke : Rs 69"): currentPrice = 69

    
    price[noOfHits] = currentPrice

    
def temp(choice):
    choice = msg.get()
    

now = datetime.now()
data = now.strftime("%A , %d-%m-%Y %H:%M")

window = Tk()
window.geometry("500x390")
window.title("Pizza Hut Bill Calculation Dashboard")

bgImg = PhotoImage(file="bg.png")
bgLabel = Label(window,image=bgImg)
bgLabel.pack()

heading = Label(window,text="Pizza Hut",font=("Cambria",30),bg="Black",fg="White")
heading.place(x = 160)

menu = ["Country Feast Pizza : Rs 529","Farmers Pick Pizza : Rs 529","Tandoori Paneer Pizza : Rs 529","Chicken Sausage n Tikka Pizza : Rs 569",
        "Chicken Tikka Pizza : Rs 569","Smoked Chicken Pizza : Rs 569","Double Cheese Pizza : Rs 419","Spiced Chicken Meatballs Pizza : Rs 469",
        "Coke : Rs 69"]

msg = StringVar(window)
msg.set(menu[0])

timeDate = Label(window,text=data,font=("Times New Roman",15),bg="Light Gray")
timeDate.place(x=140,y=50)

label1 = Label(window,text="Customer's name : ",font=("Times New Roman",15),bg="Light Gray")
label1.place(x=3,y=90)

label2 = Label(window,text="Customer's Mobile Number : ",font=("Times New Roman",15),bg="Light Gray")
label2.place(x=3,y=120)

label3 = Label(window,text="Customer's Email ID : ",font=("Times New Roman",15),bg="Light Gray")
label3.place(x=3,y=150)


entryBox1 = Entry(window,width=25,bg="Light Yellow",font=("Times New Roman",13),fg="Black")
entryBox1.place(x=260,y=93)

entryBox2 = Entry(window,width=25,bg="Light Yellow",font=("Times New Roman",13),fg="Black")
entryBox2.place(x=260,y=123)

entryBox3 = Entry(window,width=25,bg="Light Yellow",font=("Times New Roman",13),fg="Black")
entryBox3.place(x=260,y=153)

label4 = Label(window,text="Select something to order from the menu : ",font=("Times New Roman",15),bg="Light Gray")
label4.place(x=50,y=230)

dropDown = OptionMenu(window,msg,*menu,command=temp)
dropDown.place(x=105,y=260)

label5 = Label(window,text="Number of the stuff : ",font=("Times New Roman",15),bg="Light Gray")
label5.place(x=50,y=295)

entryBox4 = Entry(window,width=10,bg="Light Yellow",font=("Times New Roman",13),fg="Black")
entryBox4.place(x=230,y=298)

addButton = Button(window,text="Add to Order",bg="Red",fg="White",font=("Times New Roman",15),command=addToOrder)
addButton.place(x=370,y=270)

submitButton = Button(window,text="Submit",bg="Black",fg="White",font=("Times New Roman",15),command=display)
submitButton.place(x=220,y=335)

window.mainloop()
