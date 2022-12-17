print("Hipotenüs Hesaplayıcı")

a = float(input("Dikey Kenar :"))
b = float(input("Yatay Kenar :"))

c = a**2 + b**2

d = c ** 0.5

e =round(d,1)


print("Sonuç : {: .0f}".format(e))
