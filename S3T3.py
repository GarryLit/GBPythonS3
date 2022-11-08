#Напишите программу, которая будет преобразовывать десятичное число в двоичное

def in_numb(s):
    while 1:
        num = (input (s))
        if num == '0' or num == '' :
            print('число не должно быть равно нулю')
            continue
        else:    
            return num
            break

def dec_to_bin(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b

numb = int(in_numb('Введите десятичное число '))
print (numb)
print(dec_to_bin(numb))
         
