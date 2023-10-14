import random

choicse = ["p", "r", "s"]

Myrandom_choicse = random.choice(choicse)
print(Myrandom_choicse)

print("อาวุธ มี r = ค้อน, s = กรรไกร, p = กระดาษ")

while True:
    Mychoicse = input("ป้อนอาวุธของคุณ :")

    if Mychoicse==Myrandom_choicse:
        print(f"ผลการดวล=> เสมอ {Mychoicse} vs {Myrandom_choicse}")
    elif Mychoicse=="r" and Myrandom_choicse=="s":
        print(f"ผลการดวล=> คุณชนะ คุณออก={Mychoicse} vs บอทออก={Myrandom_choicse}")
    elif Mychoicse=="s" and Myrandom_choicse=="p":
        print(f"ผลการดวล=> คุณชนะ คุณออก={Mychoicse} vs บอทออก={Myrandom_choicse}")
    elif Mychoicse=="p" and Myrandom_choicse=="r":
        print(f"ผลการดวล=> คุณชนะ คุณออก={Mychoicse} vs บอทออก={Myrandom_choicse}")
    else:
        print(f"ผลการดวล=> คุณแพ้ คุณชนะ={Mychoicse} vs บอทออก={Myrandom_choicse}")
    
    Rematch = input("คุณต้องการดวลอีกครั้งหรือไม่ (Y/N):")
    if Rematch.upper()=="N":
        print("ไว้แวะมาดวลใหม่นะฮ๊ะ จุ๊ฟมั่วฟ")
        break
    elif Rematch.upper()=="Y":
        print("จัดไปครัชพรี่")

    else:
        print("ถือว่านายอยากเล่นอีกละกันนะ")