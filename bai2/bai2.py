tendem = str(input("Nhap ten dem: "))
n = int(input("Nhap n bang so ki tu cua moi chu cai trong ten dem vao: "))
s = 0
for i in range(0, len(str(n))):
    s = s + (n % 10)
    n = int(n / 10)
print(tendem)
print(s)