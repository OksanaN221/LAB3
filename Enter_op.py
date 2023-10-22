import random

def Enter_options(A, B, C, D, E, F):
    code1 = ''
    code2 = ''
    letters_list = 'abcdefghijklmnopqrstuvwxyz'
    num_list1 = str(D) + str(E) + str(F)
    num_list2 = str(A) + str(B) + str(C)

    for i in range(3):
        code1 += random.choice(letters_list)
    code1 += num_list1
    for i in range(3):
        code2 += random.choice(letters_list)
    code2 += num_list2

    summa = int(code1[3:]) + int(code2[3:])
    if summa < 1000:
        ans = '0' + str(summa)

    text = code1 + '-' + code2 + ' ' + ans
    return text



# print(Enter_options('1', '2', '3', '4', '5', '6'))