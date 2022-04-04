sym = {'0': 0, '': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

s = input("Введите число в шестнадцатиричной системе счисления: ")
if ',' in s:
    cel, flo = s.split(',')
else:
    cel, flo = s, ''

cel_10, flo_10 = 0, 0
j = len(cel) - 1
while j >= 0:
    for i in range(0, len(cel)):
        cel_10 += sym[cel[i]] * 16 ** j
        j -= 1
for i in range(0, len(flo)):
    flo_10 += sym[flo[i]] * 16 ** -(i + 1)
print(cel_10 if flo_10 == 0 and cel_10 != 0 else str(cel_10) + ',' + str(flo_10)[2:])


