#4 - Задайте число N. Составьте список чисел Фибоначчи, N - количество чисел в списке



def in_numb(s):
    while 1:
        num = int(input (s))
        if num == '0' or num == '' :
            print('число не должно быть равно нулю')
            continue
        else:    
            return num
            break

def fibgen():
    l = [0]
    n = in_numb("Укажите длину ряда-")
    f = 1   # first
    s = 0   # second
    i = 2
    while (i < n+1):
        print(i)
        a = s
        l.insert(i, f+s)
        if (i == 0):
            s = 1
            f = 0    
        i += 1
        a = f
        f = s
        s = a + s
        
    return(l)
    
 
print(fibgen()) 
