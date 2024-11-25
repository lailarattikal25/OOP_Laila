num = {}
default = int(input("ต้องการป้อนทั้งหมดกี่ตัว"))
for i in range(1,default+1):
    print(f'จำนวนคนที่ {i}')
    num['nickname'] = (str(input('กรุณากรอกชื่อเล่น : ')))
    num['stdid'] = (int(input(f'กรุณากรอกเลขที่  : ')))
    num['hobby'] = (str(input('กรุณากรอกงานอดิเรก : ')))
    num['color'] = (str(input('กรุณากรอกสีที่ชอบ : ')))
    print(f"ข้อมูลคนที่ {str(i)}\n{num}")