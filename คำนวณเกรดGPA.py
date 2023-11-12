#การคำนวณเกรด GPA เหมือนคำนวณเกรดเฉลี่ยของโรงเรียน
"""
1.ต้องรู้ว่า เรียนกี่วิชา, เกรดแต่ละวิชา, หน่วยกิตแต่ละวิชา(ชั่วโมงเรียน)
2.นำเกรดมาคูณกับหน่วยกิตของแต่ละวิชามาบวกกัน
3.ข้อ2 หารกับหน่วยกิตทุกวิชารวมกัน
"""

def Cal_GPA(Subject):
    Unit_time = 0
    Sum_Sub_Time = 0
    for sub in range(1, Subject+1):
        Grade = float(input(f"วิชาที่ {sub} ได้เกรดอะไร :"))
        Time = float(input(f"วิชาที่ {sub} กี่หน่วยกิต :"))
        Unit_time += Grade*Time
        Sum_Sub_Time += Time
    Calculate_grade = Unit_time/Sum_Sub_Time
    return Calculate_grade if Calculate_grade<=4 and Calculate_grade>=0 else 4


How_many_subject = int(input("คุณเรียนกี่วิชา :"))
print(f"เกรดของคุณ = {Cal_GPA(How_many_subject)}")