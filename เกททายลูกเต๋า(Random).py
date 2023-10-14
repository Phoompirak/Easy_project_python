#เกมทายลูกเต่า
import random

myrandom=random.randrange(1,7)
k=1
correct=False
print("คุณมีโอกาสตอบแค่3ครั้ง \n")
while True:
    number=int(input("ป้อนคำตอบของคุณ :"))
    correct=(number==myrandom)

    if not correct:
        if(number>myrandom):
            print("น้อยกว่า")
        if(number<myrandom):
            print("มากกว่า")
        
    if correct:
        print("ตอบถูกจร้าาาา")
        break
    k+=1
    if number<0 or k==3:
        break
       
if not correct:
    print("เฉลย =",myrandom)
    print("จบโปรแกรม")