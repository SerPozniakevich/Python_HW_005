#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#Входные и выходные данные хранятся в отдельных текстовых файлах.



arh_t = []
unarh_t = []
patch = 'file.task_003.txt' 
f = open(patch, 'r')
t = f.read() 
print(t)

counter = 1
for i in range(len(t) - 1):
    if i <= len(t):
        if t[i] == t[i + 1]:
            counter += 1
        else:
            arh_t.append(counter)
            arh_t.append(t[i])
            counter = 1
arh_t.append(counter)
arh_t.append(t[i])
print(*arh_t)

j = 0
while j in range(len(arh_t) - 1):
    unarh_t.append(arh_t[j] * arh_t[j + 1])
    j += 2

unarh_t = str(unarh_t).replace(" ","")

with open('file.task_003.unarh_t.txt', 'a') as data:
    data.write(str(unarh_t))

