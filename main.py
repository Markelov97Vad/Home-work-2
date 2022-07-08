l = [65, 17, 2, 45, 3, 233, 97]
print(l)
Max = l[0]
Min = l[0]
del_na = l[0]
for i in range(len(l)):
    if l[i] > Max:
        Max = l[i]
    if l[i] < Min:
        Min = l[i]
    if l[i] % 3 == 0 and l[i] % 5 != 0:
        del_na = l[i]

# делятся на 3 и не делятся на 5
print(Max, Min, del_na)