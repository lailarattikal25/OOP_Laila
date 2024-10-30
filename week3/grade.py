print("โปรแกรมคำนวณเกรดเฉลี่ย")
grade = int(input("กรอกคะแนน : "))
if grade >= 100 :
    print("error")
elif grade >= 80 :
    print("คุณได้เกรด 4 ")
elif grade >= 70 :
    print("คุณได้เกรด 3 ")
elif grade >= 60 :
    print("คุณได้เกรด 2 ")
elif grade >= 50 :
    print("คุณได้เกรด 1 ")
elif grade <50 :
    print("คุณสอบตก")
    print("คุณต้องการแก้ 0 ไหม")
    take2 = int(input("ถ้าใช่ ตอบ1 ถ้าไม่ ตอบ 2 \n คำตอบคือ : " ))
    if take2 == 1:
        print("คุณขาดคะแนนอีก "+str(50-grade)+"ถึงจะสอบผ่าน")
    elif take2 == 2:
        print("คุณสอบแก้ไม่ผ่าน")
else :
    print("กรอกตัวเลขใหม่อีกครั้ง")