import fitz # PyPDF
import io
from PIL import Image

file = 'D:\python\Easy_project_python\ดูดรูปจากPD\pp.pdf'
try:
    pdf_file = fitz.open(file)
except NameError: 
    print(f"ชื่อไฟล์หรือโฟลเดอร์ไม่ถูก => {NameError}")
except FileNotFoundError:
    print(f"หาไฟล์ไม่เจอ => {FileNotFoundError}")
except Exception as e: # Error อย่างอื่นที่ไม่ได้ดัก
    print(e)

print (f"มีหน้าPDF = {len(pdf_file)} หน้า")

for page_index in range(len(pdf_file)):
    page = pdf_file[page_index]
    print(page)
    
    image_list = page.get_images()

    for image_index, img in enumerate(image_list, start=1):
        print(f"หน้าที่ {page_index+1} มี {image_index} รูป")
        
        xref = img[0]
        base_image = pdf_file.extract_image(xref)
        
        image_bytes = base_image["image"]
        image_extention = base_image["ext"]
        
        image = Image.open(io.BytesIO(image_bytes))
        print(image)
        image.save(open(f"D:\python\Easy_project_python\ดูดรูปจากPDF\image_2\image{page_index+1}_{image_index}.{image_extention}","wb"))
    
print('success')