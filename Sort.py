#Массив имен людей и их возраста
employees = [
    ["Валера", 30],
    ["Иван", 25],
    ["Андрей", 28],
    ["Олег", 51],
    ["Вася", 22],
    ["Александр", 34]
]

def custom_key(people):
    return people[1]  # Сортировка по возврату

employees.sort(key=custom_key)
print(employees)

