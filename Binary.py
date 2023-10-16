from tkinter import *

#หาร2 ถ้ามีเศษเหลือก็จะเป็นเลข1 ถ้าไม่ก็เลข0 ไปเรื่อยจนเหลือ0
def Decimal_to_Binary():
    Number = int(entry.get())
    Binary = ""
    while Number>0:
        if Number%2 != 0:
            Binary = Binary+"1"
        else:
            Binary = Binary+"0"
        Number = Number//2

    #เมื่อหารด้วย2แล้วตามสูตรต้องอ่านจากขวาไปซ้าย
    Reverse_Binary = ""
    N = len(Binary)-1
    while N>=0:
        Reverse_Binary = Reverse_Binary+Binary[N]
        N-=1
    
    
    label.configure(text=f"Your decimal number :{Reverse_Binary}")
    

def Binary_to_Decimal():
    Number = str(entry.get())
    Decimal = 0
    Reversed_Number = ""
    N = len(Number)-1
    while N>=0:
        Reversed_Number = Reversed_Number+Number[N]
        N-=1

    for i in range(len(Reversed_Number)):
        if Reversed_Number[i] == "1":
            Decimal += 2**i
    

    label.configure(text=f"Your binary number :{Decimal}")


def input_Binary_or_Deciaml():
    label2 = entry.get()
    if label2.lower() == "d":
        label.configure(text="Please insert Decimal:")
        submit_button.configure(command=Decimal_to_Binary)
    elif label2.lower() == "b":
        label.configure(text="Please insert Binary:")
        submit_button.configure(command=Binary_to_Decimal)


window = Tk()
window.title("Binart_and_Decimal")
window.geometry("420x420")
window.config(background="#a2add0")

#ป้ายชื่อ
label = Label(window,
text="Please insert Binary or Decimal:",
font=('consolas', 15, 'bold'),
fg='#00FF00',bg='#999999',relief=RAISED,bd=10,)
label.pack() #Label.place(x=0, y=0) เพื่อแสดงมุมซ้าย

entry = Entry(window, font=("Arial", 15))
entry.pack(pady=20)

submit_button = Button(window, text="submit", command=input_Binary_or_Deciaml)
submit_button.pack()

window.mainloop() #เริ่มวางหน้าต่าง