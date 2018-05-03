def pereplata(sum, term, rate):
    pct = rate / 100 / 12
    month_pay = pct * pow((1 + pct), term) / (pow((1 + pct), term) - 1)
    return round(((sum * month_pay) * term) - sum, 2)

perepl = pereplata(2000000, 60, 10)
print('Переплата: ', perepl)
#Переплата:  549645.37