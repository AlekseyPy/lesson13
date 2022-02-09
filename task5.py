number = int(input("Введите число n: "))
for i in range(1,number+1):
    spisok = {
        i:i**2
}
    for g in spisok.values():
        print(f"Квадрат числа n = {g}")
