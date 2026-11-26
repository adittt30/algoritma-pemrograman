x = 2
y = 1
print("X =", x ,"Y =", y)

print("Bagian A: Urutan naik")
for i in range(1 + 10 + x + 1):
    print(i)

print("Bagian B: Kelipatan 2")
for i in range(2, 2 * (5 + y) + 1, 2):
    print(i)

print("Bagian C: Urutan mundur")
for i in range(10 + x, 0, -1):
    print(i)