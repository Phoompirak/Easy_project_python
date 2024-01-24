import ffmpeg
import os

# ชื่อไฟล์ต้นฉบับ
input_filename = "pyconvert\\20240118_145626.mov"

# โหลดไฟล์วิดีโอ
input_video = ffmpeg.input(input_filename)

# บีบอัดวิดีโอด้วยอัลกอริธึม H.265
output_video = input_video.output("output.mov", codec="libx265")
# print(os.listdir("\\convert_mp4\\pyconvert")) # เช็คไฟล์ในโฟลเดอร์ (ไม่ต้องมีก็ได้)

# ตรวจสอบขนาดไฟล์ต้นฉบับ
input_size = os.path.getsize(input_filename)  # ใช้ชื่อไฟล์ต้นฉบับที่นี่

try:
    # ตรวจสอบขนาดไฟล์บีบอัด (หลังจากการบีบอัดเสร็จสิ้น)
    output_size = os.path.getsize("output.mov")  # แก้ไขเส้นทางถ้าจำเป็น

    # เปรียบเทียบขนาดไฟล์
    if input_size > output_size:
        print("ย่อขนาดไฟล์สำเร็จ")
        print(f"Size => {output_size}")
    else:
        print("ย่อขนาดไฟล์ไม่สำเร็จ")
except FileNotFoundError:
    print("เกิดข้อผิดพลาด: ไม่พบไฟล์ output.mov โปรดตรวจสอบการบีบอัด")