#Размер массива
n = 3
m = 4

#Массив
d5 = []

#Цикл внешний
for i in range(m):
    # Создание размера = i массива
    d5.append([])

    #Цикл внутренний
    for j in range(n):
        #Устанавливаем значение 5 всем элементам массива
        d5[i].append(5)

print(d5)
# Output: [[5, 5, 5], [5, 5, 5], [5, 5, 5], [5, 5, 5]]