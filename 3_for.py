"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
sales = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]

def all_phone_sales(phone_sales):
    phone_sum = 0
    for phone in phone_sales:
      phone_sum += phone
    return phone_sum 


def all_phone_sales_average(phone_sales):
    phone_sum = 0
    for phone in phone_sales:
      phone_sum += phone
    return phone_sum /len(phone_sales)
    
phones_sum = 0    
for one_phones in sales:
    all_phone_sum = all_phone_sales(one_phones['items_sold'])
    print(f'Суммарное количество продаж для  {one_phones["product"]}: {all_phone_sum}') 
    phone_average = all_phone_sales_average(one_phones['items_sold'])
    print(f'Среднее количество продаж для  {one_phones["product"]}: {phone_average}') 
    
    phones_sum += all_phone_sum
    phones_sum_average = all_phone_sum / len(sales)

#print(phone_sales)
print(f'Суммарное количество продаж для всех товаров: {phones_sum}')  
print(f'Среднее количество продаж всех товаров: {phones_sum_average}')  

if __name__ == "__main__":
      print('Конец')
