x = 24
z = ""

# if x >= 1000:
#     y = 3
#     while y > 0 and x >= 1000:
#         x = x - 1000

# if x >= 500:
#     y = 3
#     while y > 0 and x >= 500:
#         x = x - 500

# if x >= 100:
#     y = 3
#     while y > 0 and x >= 50:
#         x = x -100

# if x >= 50:
#     y = 3
#     while y > 0 and x >= 50:
#         x = x - 50

if 5 < x >= 1:
    y = 3
    while y > 0 and x >= 1:
        x = x - 1
        z = z + "I"
        y = y - 1

if x >= 5:
    y = 3
    while y > 0 and x >= 5:
        x = x - 5
        z = z + "V"
        y = y - 1

if x >= 10:
    y = 3
    while y > 0 and x >= 10:
        x = x - 10
        z = z + "X"
        y = y - 1


print(f"resto: {x}")
print(f"Numero romano: {z}")

