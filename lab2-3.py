print("------------คำนวณค่าดัชนีมวลกาย------------")
w = float(input("น้ำหนักตัว: "))
h = float(input("ส่วนสูง: "))
x = (h/100)**2
y = w/x
print("ค่าดัชนีมวลกายคือ %.2f" %y)

if y < 18.50 :
    print("น้ำหนักน้อย/ผอม")
elif y >=18.50 and y <=22.90 :
    print("---ปกติ(สุขภาพดี)---")
elif y >=23 and y <=24.90 :
    print("---ท้วม/โรคอ้วนระดับ 1---")
elif y >=25 and y <=29.90 :
    print("---อ้วน/โรคอ้วนระดับ 2---")
elif y >=30 :
    print("---อ้วนมาก/โรคอ้วนระดับ 3---")    