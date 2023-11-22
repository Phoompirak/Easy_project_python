"""
ผู้ที่ได้คะแนนตั้งแต่ 90 คะแนนขึ้นไปจะได้เกรด A
ผู้ที่ได้คะแนนตั้งแต่ 85 - 89 จะได้เกรด B+
ผู้ที่ได้คะแนนตั้งแต่ 80 - 84 จะได้เกรด B
ผู้ที่ได้คะแนนตั้งแต่ 75 - 79 จะได้เกรด C+
ผู้ที่ได้คะแนนตั้งแต่ 70 - 74 จะได้เกรด C
ผู้ที่ได้คะแนนตั้งแต่ 65 - 69 จะได้เกรด D+
ผู้ที่ได้คะแนนตั้งแต่ 60 - 64 จะได้เกรด D
ผู้ที่ได้คะแนนต่ำกว่า 60 ลงไปจะได้เกรด F
"""

def grading(average):
  if average < 0:
    return
  grade = "FFFFFDCBAAA"
  if average % 10 >= 5:
    if grade[average // 10] == "A":
      return "A"
    elif grade[average // 10] == "F":
      return "F"
    return grade[average // 10] + "+"
  else:
    return grade[average // 10]


print(grading(sum([int(input()) for i in range(3)])))