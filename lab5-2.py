def Ex(n):
    total_sum = 0
    for i in range(n):
        price = float(input("รายการสินค้าที่ %d ราคา: " % (i+1)))
        total_sum += price
        
    total_with_vat = total_sum * 1.07
    return total_with_vat

n= int(input("จำนวนสินค้า: "))
total_price = Ex(n)
print("ราคาทั้งหมด: %.2f" % total_price)

paid_amount = float(input("จำนวนเงินที่จ่าย: "))
change = paid_amount - total_price
print("จำนวนเงินทอน: %.2f" % change)