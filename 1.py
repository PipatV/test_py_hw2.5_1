# User input
income = int(input())
# สามารถเปลื่ยนตัวแปร r,n ให้ไดนามิคมากขึ้น
r = 5/100
n = 10

# ลูปตามจำนวน n เริ่มที่ 1, สิ้นสุด n+1
for i in range(1,(n+1)):

    # คำนวณ a
    a = income*(1+r)**(i)

    # แสดงผล
    print("ฝากเงิน",i,"ปี " + "จำนวนเงิน",a)