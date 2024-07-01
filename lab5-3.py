def Ex(h, m, f):
    total_score = h + m + f
    return total_score

def bmi(score):
    if score > 80:
        result = "คะแนนมากกว่า 80 คะแนน ดีมาก"
    elif score >= 51 and score <= 79:
        result = "คะแนนมากกว่า 50 คะแนน ผ่าน"
    elif score >= 0 and score <= 50:
        result = "คะแนนน้อยกว่า 50 คะแนน ไม่ผ่าน"
    return result

h = int(input("คะแนนกานบ้าน (ไม่เกิน 20 คะแนน): "))
while h > 20:
    print("ไม่สามารถใส่คะแนนมากกว่า 20 คะแนนได้")
    h = int(input("กรุณาใส่คะแนนการบ้านใหม่ (ไม่เกิน 20 คะแนน): "))
    
m = int(input("คะแนนสอบกลางภาค (ไม่เกิน 40 คะแนน): "))
while m > 40:
    print("ไม่สามารถใส่คะแนนมากกว่า 40 คะแนนได้")
    m = int(input("กรุณาใส่คะแนนสอบกลางภาค (ไม่เกิน 40 คะแนน): "))
    
f = int(input("คะแนนสอบปลายภาค (ไม่เกิน 40 คะแนน): "))
while f > 40:
    print("ไม่สามารถใส่คะแนนมากกว่า 40 คะแนนได้")
    f = int(input("กรุณาใส่คะแนนสอบปลายภาค (ไม่เกิน 40 คะแนน): "))
    
total_score = Ex(h, m, f)
result_message = bmi(total_score)
print("ผลลัพธ์: ", result_message)