num = []
section = int(input("ต้องการป้อนทั้งหมดกี่ตัว"))
for i in range(1,section+1):
    section = (int(input(f'ใส่ตัวที่ {i} : ')))
    num.append(section)
result = sum(num)//len(num)
print(f"ค่าเฉลี่ยของ คือ {num} = {result}")