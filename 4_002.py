import random


def result_print(sum_result, number):
    if number == 1:
        print("Введенные данные: " + str(sum_result))
    else:
         print("Ответ: " + str(sum_result))

def list_check():
    h = []
    for i in range(0, len(n)):
        m = 0
        for j in range(0, len(n)): 
            if n[j] == n[i] and i != j:
                m = 1

        if m == 0:
            h.append(n[i])

    result_print(h, 0)
    
        
def list_creat():
    i = 0
    while i < 1:
        input_man = int(input("Введите число для добавления в массив или 0 для завершения: "))
        if input_man == 0:
            result_print(n, 1)
            break
        else:
             n.append(input_man)

n = []
list_creat()
list_check()