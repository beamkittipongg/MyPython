def circle(radius):
    area = 22/7*(radius*radius)
    return area
R = int(input("ค่ารัศมี: "))
print("พื้นที่วงกลม %.3f" % circle(R))