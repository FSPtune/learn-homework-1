"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""
def main():

    write_age = int(input())
    if 3 <= write_age < 7:
        return 'Учиться в детском саду'
    elif 7 <= write_age < 15:
        return 'Учиться в школе'
    elif 15 <= write_age < 100:
        return 'Учиться в Вузе или работать'
    else:
        return 'Что-то пошло не так'


if __name__ == "__main__":
   print(main())
    