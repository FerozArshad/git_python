enc = "utf-8"
a = open(r"C:\Users\feroz\OneDrive\Desktop\a.txt" , "a" , encoding=enc)
a.write('Hello New Line\n')
a.close()

b = open(r"C:\Users\feroz\OneDrive\Desktop\a.txt" , "r" , encoding=enc)
c = b.readlines()
print(*c , sep="\n")