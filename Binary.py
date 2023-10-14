#หาร2 ถ้ามีเศษเหลือก็จะเป็นเลข1 ถ้าไม่ก็เลข0 ไปเรื่อยจนเหลือ0

def Decimal_to_Binary(Number):
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
    return Reverse_Binary
    

def Binary_to_Decimal(Number):
    Decimal = 0
    Reversed_Number = ""
    N = len(Number)-1
    while N>=0:
        Reversed_Number = Reversed_Number+Number[N]
        N-=1

    for i in range(len(Reversed_Number)):
        if Reversed_Number[i] == "1":
            Decimal += 2**i
    return Decimal

            

Insert = input("Please insert Decimal or Binaly:")

if Insert.lower() == "d":
    Number = int(input("Please insert Decimal:"))
    print(Decimal_to_Binary(Number))

else:
    Number = input("Please insert Binary:")
    print(Binary_to_Decimal(Number))