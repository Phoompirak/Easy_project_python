
Hour = int(input("ป้อนชั่วโมงที่ใช้บริการ :"))
Member = input("คุณไดสมัครสมาชิกหรือไม่? (Yes,No):")
Bath_per_hour = 15
Total_pay = Hour*Bath_per_hour if Member.lower() in "n" else Hour*Bath_per_hour-(Hour*Bath_per_hour*0.1)+100


print(f"เงินที่ต้องจ่าย {Bath_per_hour}/Hour = {Total_pay}") if Hour >= 0 else print("เกิดข้อผิดพลาดในการป้อน")