def words(num):
    titles = ['товар', 'товара', 'товаров']
    cases = [2, 0, 1, 1, 1, 2]

    a = 0
    if num % 100 > 4 and num % 100 < 20:
        a = 2
    else:
        a = (cases[min(num % 10, 5)])

    print(num, titles[a])


words(0)
words(1)
words(3)
words(4)
words(5)
words(10)
words(22)
words(23)
