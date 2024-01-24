import os
import subprocess

my_dir = '..\\video\\MEME_crazy.mp4' # ป้อนที่อยู่ไฟล์
find_dir = os.path.exists(my_dir)
print(f"find directory => {find_dir}") #เช็คตรงนี้ อยู่ๆก็ใช้ได้

add_skipped = 0
for fn in os.listdir(my_dir):
    print(f"IS file => {os.path.isfile(fn)}") #เช็คตรงนี้ อยู่ๆก็ใช้ได้
    if os.path.isfile(fn):
        if fn.endswith(".mp4"): # เช็คว่าไฟล์นามสกุลไร
            print("mp4 file found: " + fn)
            p = subprocess.run(
                ["ffmpeg",
                "-i", fn,
                "-n",
                "-acodec", "copy",
                "-vcodec", "copy",
                "-f", "mov", fn[:-4] + ".mov"], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=False)
            if p.returncode == 0: # เช็คว่า โค้ดlibrary return 0 = รันโค้ดผ่าน ไหม
                os.remove(fn)
                print("Converted " + fn)
            else:
                add_skipped += 1 # ตัวแปรสำหรับเช็คว่าข้ามไฟล์ไฟล์ที่ไม่สามารถแปลงได้ไปกี่ไฟล์
                print("Skipped   " + fn)

print(f"$Procecs success$,\nSkip file=>{add_skipped}")