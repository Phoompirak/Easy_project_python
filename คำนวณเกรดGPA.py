#การคำนวณเกรด GPA เหมือนคำนวณเกรดเฉลี่ยของโรงเรียน

def Cal_GPA(Subject):
    Unit_time = 0
    Sum_Sub_Time = 0
    for sub in range(1, Subject+1):
        Grade = float(input(f"วิชาที่ {sub} ได้เกรดอะไร :"))
        Time = float(input(f"วิชาที่ {sub} กี่หน่วยกิต :"))
        Unit_time += Grade*Time
        Sum_Sub_Time += Time
    Calculate_grade = Unit_time/Sum_Sub_Time
    return Calculate_grade


How_many_subject = int(input("คุณเรียนกี่วิชา :"))
print(f"เกรดของคุณ = {Cal_GPA(How_many_subject)}")