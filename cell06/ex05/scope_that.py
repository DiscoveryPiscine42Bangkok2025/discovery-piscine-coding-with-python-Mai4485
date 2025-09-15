def add_one(n):
    return n + 1
x = 5
print("Before:", x)
x = add_one(x)
print("After:", x) #add_one(x) ไม่เปลี่ยนค่า x เดิม int ใน Python เป็น immutable

# def add_one(n):
#     return n + 1
# x = 5
# print("Before:", x)
# x = add_one(x) //6
# print("After:", x) 
