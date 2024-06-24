def circle(h,w):
    c = (h/100)**2
    b = w/c
    return b
def bmi (n):
    if n<18.50:
        print("น้ำหนักน้อย/ผอม")
    elif n>=18.50 and n<=22.90 :
        e = ("ปกติสุขภาพดี")
    elif n>=24.90 and n<=23 :
        e = ("ท้วน")
    elif n>=25 and n<=29.90 :
        e = ("อ้วน")
    elif n>30 :
        e = ("อ้วนมาก")
    return e

x = float (input("ส่วนสูง: "))
z = float (input("น้ำหนัก: "))
n = circle(x,z)
bmi1 = bmi(n)

print("ค่าดัชนีมวลกายคือ %.3f" %n)
print("ค่าดัชนีมวลกายอยู่ในเกณฑ์ ", bmi1)