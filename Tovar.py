import pymorphy2
import string

#"Plural-Forms: nplurals=3;
# n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);
# (num % 100 > 4 && num % 100 < 20) ? 2 : cases[Math.min(num % 10, 5)]];

def words(num):
    titles = ['товар', 'товара', 'товаров']
    cases = [2, 0, 1, 1, 1, 2]

    print(num % 100 > 4 & num % 100 < 20)
    print((num % 10, 5))


    a = 0
    if (num % 100 > 4 & num % 100 < 20): a = 2
    else: a = (cases[min(num % 10, 5)])

    print(num, titles[a])
    #(num % 100 > 4 && num % 100 < 20)

#    return titles[(num % 100 > 4 & num % 100 < 20): 2, cases[min(num % 10, 5)]]

#    a = 0
##    if (num%10==1 & num%100!=11): a = 0
#    elif (num%10>=2 & num%10<=4 & (num%100<10 | num%100>=20)): a = 1
#    else: a = 2

#    print(a)
#    print(num, titles[a])

#"Plural-Forms: nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);\n"

#    return num + ' ' + titles[(num % 100 > 4 && num % 100 < 20) ? 2 : cases[Math.min(num % 10, 5)]];
# nplurals=3; plural=(n%10==1 && n%100!=11 ? 0 : n%10>=2 && n%10<=4 && (n%100<10 || n%100>=20) ? 1 : 2);


words(0)
words(1)
words(3)
words(4)
words(5)
words(10)
words(22)
#words(23)