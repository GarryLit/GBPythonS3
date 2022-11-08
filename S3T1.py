# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def mult_sp(sp):
    rez = []
    l = len(sp)-1
    for i in range(l):
        rez.append(sp[i] * sp[l - i]) 
    return rez

sp = [2, 3, 5, 6, 8]
print(mult_sp(sp))