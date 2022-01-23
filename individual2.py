x = float(input("Введите координату x: "))
y = float(input("Введите координату y: "))
if (x*x + y*y <=1) and (x*x + y*y >= 0.25):
    print("Принадлежит")
else:
    print("Не принадлежит")