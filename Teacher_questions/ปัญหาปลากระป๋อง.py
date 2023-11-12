#หลายจุดประสงค์
""" import numpy as np
Fish = int(input("ป้อนจำนวนปลาซาร์ดีน :"))
Tomato = int(input("ป้อนจำนวนมะเขือเทศ :"))

def cal_factory(Fish, Tomato):
    factory_min = np.min(Fish//3, Tomato//2)
    remain_fish = Fish-factory_min*3
    remain_tomato = Tomato-factory_min*2
    return factory_min, remain_fish, remain_tomato

print(f"ผลิตปลากระป๋องได้ทั้งหมด :{cal_factory(Fish, Tomato)[0]}")
print(f"คงเหลือปลาซาร์ดีน :{cal_factory(Fish, Tomato)[1]}")
print(f"คงเหลือมะเขือเทศ :{cal_factory(Fish, Tomato)[2]}")
"""


#เชิงสัญลักษณ์
""" x = int(input("ป้อนจำนวนปลาซาร์ดีน :")) #จำนวนปลาซาร์ดีน
Tomato = 200//2  #จำนวนมะเขือเทศ

print("xหาร3 = ",x//3)
if x>=3 and x<=300:
    print(f"ผลิตปลากระป๋องได้ :{x//3}")
elif x>300:
    print(f"ผลิตปลากระป๋องได้ :{}")

else:
    print("ไม่สามารถผลิตปลากระป๋องได้") """

M = int(input("ป้อนจำนวนปลาซาร์ดีน :")) #จำนวนปลาซาร์ดีน/1กระป๋อง 
Tomato = 2  #จำนวนมะเขือเทศ/1กระป๋อง
Total_M = 600//M
Total_Tomato = 200//Tomato
MIN_TOTAL = min(Total_M, Total_Tomato)

if M>=1:   
    if M==600:
        print(f"ผลิตปลากระป๋องได้ทั้งหมด :600หารM = {1}")
    elif M>600:
        print("ปลาไม่พอ")
    print(f"ผลิตปลากระป๋องได้ทั้งหมด :600หารM = {Total_M}")
else:
    print("ไม่สามารถหาค่าได้")