print("ประวัติส่วนตัว")
name = str(input('กรุณากรอกชื่อ-นามสกุล :'))
nickname = str(input('กรุณากรอกชื่อเล่น :'))
age = int(input('กรุณากรอกอายุ :'))
ID = int(input('กรุณากรอกเลขประจำตัวนักศึกษา :'))
level = int(input('กรุณากรอกระดับชั้น :'))
height = float(input('กรุณากรอกส่วนสูง :'))
weignt = float(input('กรุณากรอกน้ำหนัก :'))
result = height+weignt
print("ชื่อ : "+name+"=ชื่อเล่น : "+nickname)
print("อายุ : "+str(age)+"รหัสประจำตัวนักศึกษา : "+str(ID)+"ระดับชั้น : "+str(level))
print("ส่วนสูง : "+str(height)+"น้ำหนัก : "+str(weignt))
print("ส่วนสูง + น้ำหนัก = "+str(result))