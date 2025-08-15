# คำสั่งรับค่าข้อความ ใช้ฟังก์ชั่น รinput()
# ***** ตัวแปร veriable คือ ชื่อที่ dav ตั้งขึ้นเอง เป็นไปตามกฎการตั้งชื่อ หน้าที่เก็บข้อมูลที่ใช้ในโปรแกรม

fullname = input('ป้อนชื่อ: ')
mid_score = input('ป้อนคะแนนกลางภาค: ')
final_score = input('ป้อนคะแนนสอบปลายภาค: ')
quiz_score = input('ป้อนคะแนนเก็บ: ')
print('..................')
print(f'สวัสดีคุณ : {fullname}')
print(f'คุณสอบได้คะแนนรวม : {int(mid_score) + int(final_score) + int(quiz_score)} คะแนน')

