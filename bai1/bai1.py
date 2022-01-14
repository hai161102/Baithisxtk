ten = str(input("Nhap ten: "))
n = int(len(ten))
print("Ten cua ban la:",ten)
print("{} ten co {} ki tu".format(ten, n))
sb = ""
for i in range(1, n+1):
    sb = sb + "{" +  str(i) + ":" + str(i*i) + "}" + ","
print(sb)