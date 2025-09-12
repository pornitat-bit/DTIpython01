# return  คือ คำสั่ง ที่ใช้ส่งข้อมูลใดๆ กลับยังจุดเรียกใช้ฟังก์ชัน/คำสั่ง return ยังเปฌนการบอกว่า

# 3. no paramiters have return 
'''
def  func_name ()
    คำสั่ง
    คำสั่ง
    ..........
    return คำสั่งที่ต้องการส่งกลับ
'''
def func_e() :
    print('Hello...')
    return 'Hi...'

def func_f() :
    return 'Wow...', 'Wooo...', 99999

print(func_e())

xx = func_e()
print(xx)

a, b, c = func_f()
print(a)
print(b)
print(c)