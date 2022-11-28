
"""
if boolean expression : #เงื่อนไขเปรียบเทียบ 
    statement1

elif boolean expression :
    statement2

else
    statement3
    
"""

#โปรแกรมเปรียบเทียบค่า 2 ค่า
"""
print("โปรแกรมเปรียบเทียบค่า 2 ค่า")
#input
print("รับค่าที่ 1 :")
a = input()         #ตัวแปร a เป็น str
a = int(a)          #ตัวแปร a เป็น int
print("รับค่าที่ 2 :")
b = input()
b = int(b) 

#process #output

if a>b :
    print("มากกว่า")
elif a<b :
    print("น้อยกว่า")
else :
    print("เท่ากับ")

print("จบการทำงานของโปรแกรม")
"""
#-------------------------------------------------
"""
#โปรแกรมค้นหาดัชนีมวลกาย
#input
print("โปรแกรมค้นหาดัชนีมวลกาย")
print("ป้อนน้ำหนักของคุณ (kg) : ")
w = input()
w = int(w)
print("ป้อนส๋วนสูงของคุณ (cm) : ")
h = input()
h = int(h) #cm

#process
h = h/100  #เปลี่ยน cm -> m
bmi = w/(h**2) #หาค่า bmi

#output
print("BMI = " , bmi)
"""
#-------------------------------------------------


#โปรแกรมค้นหาดัชนีมวลกาย
#input
print("โปรแกรมค้นหาดัชนีมวลกาย")
print("ชื่อ นามสกุล ห้อง เลขประจำตัว")

#print("ป้อนน้ำหนักของคุณ (kg) : ")
#w = input()
#w = int(w)
w = int(input("ป้อนน้ำหนักของคุณ (kg) : "))
h = int(input("ป้อนส๋วนสูงของคุณ (cm) : "))/100
#process
#h = h/100  #m
bmi = w/(h**2) 

print("ค่า BMI ของคุณคือ " , bmi)

"""
< 18.5	       คุณผอมเกินไป
18.6 - 22.9    คุณน้ำหนักปกติ
23.0 - 24.9    คุณน้ำหนักเกิน
25.0 - 29.9    คุณอ้วน
>30	           คุณอ้วนมาก"""

if bmi < 18.5 :
    print("คุณผอมเกินไป")
elif bmi >=18.6 and bmi <=22.9 :
    print("คุณน้ำหนักปกติ")
elif bmi >=23.0 and bmi <=24.9 :
    print("คุณน้ำหนักเกิน")
elif bmi >=25.0 and bmi <=29.9 :
    print("คุณอ้วน")
elif bmi > 30 :
    print("คุณอ้วนมาก")
else :
    print("ไม่ทราบค่าที่ชัดเจน")

#----------------------------------------------

#การทำงานแบบทำซ้ำ
# while loops
"""
while expression :
    statement
"""
"""
i = 1
while i<=5 :
    print("รอบที่ " , i)
    i = i+1
"""
