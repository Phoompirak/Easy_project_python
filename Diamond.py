"""
ผลลัพธ์ที่ต้องการ
   R
  DRO
 EDROO
BEDROOM
 EDROO
  DRO
   R


 OV
LOVE
 OV
"""
# สร้างlistที่มีข้อความรวมกับเว้นวรรค
def diamond_title(Title):
  Total_title = []
  Mid_title = len(Title)//2

  #แยกความยาวข้อความว่ายาวคี่หรือคู่ เพราะแพทเทิร์นในโจทย์คู่คี่แยกกัน
  if len(Title)%2 == 0:
    # Mid_title+=1
    for i in range(1, Mid_title+1):
      Total_title.append(" " * (Mid_title-i) + Title[Mid_title-i:Mid_title+i])
  else:
    for i in range(Mid_title+1):
      Total_title.append(" " * (Mid_title-i) + Title[Mid_title-i:Mid_title+i+1])

  return Total_title

# แสดงผลlistเรียงลงไปและเรียงแบบReverse
def Diamond_Squar(Total_title):
  for i in range(len(Total_title)):
    print(Total_title[i])

  for i in range(len(Total_title)-2, -1, -1):
    print(Total_title[i])


Input_title = input("ป้อนข้อความที่ต้องการ :")
# Input_title = "LOVE"
# print(diamond_title(Input_title))
Diamond_Squar(diamond_title(Input_title))