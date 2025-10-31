z = 0
y = 0
for x in range(11):
    print(f"y = {y}")
    print(f"x = {x}")
    y = x * x
    z = z + y

print(z)
y = 0
for x in range(11):
    print(x)
    print(y)
    y += x


print(y**2)
print(z)
print(y)
print((y**2)-z)